// ==========================================
// 1. WEBHOOK (Fixed: No Empty Rows + Instant Lock)
// ==========================================
function doGet(e) {
  var lock = LockService.getScriptLock();
  // Wait up to 5 seconds to prevent collisions if two people click at once
  lock.tryLock(5000); 

  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var action = e.parameter.action;

    // --- ACTION A: READ (Map is loading... just send the list) ---
    if (action == "read") {
      var data = sheet.getDataRange().getValues();
      var names = [];
      
      // We look at Column B (Index 1) for the Site Name
      // Skip the header row (i=1)
      for (var i = 1; i < data.length; i++) {
        var rowName = data[i][1]; 
        // Only add if name is NOT empty
        if (rowName && rowName.toString().trim() !== "") {
          names.push(rowName.toString());
        }
      }
      
      return ContentService.createTextOutput(JSON.stringify({'names': names}))
             .setMimeType(ContentService.MimeType.JSON);
    }

    // --- ACTION B: ADD (User clicked "Add Pod") ---
    if (action == "add") {
      var name = e.parameter.name;
      var borough = e.parameter.borough;
      var type = e.parameter.type;
      var courts = e.parameter.courts;

      // 1. SECURITY: Stop Empty Rows
      // If the map sends a blank name, we REJECT it.
      if (!name || name === "undefined" || name.trim() === "") {
        return ContentService.createTextOutput(JSON.stringify({'result': 'error', 'message': 'Empty Name'}));
      }

      // 2. CHECK DUPLICATES (Server-Side)
      // We normalize strings to catch "Hyde Park" vs "hyde park"
      var data = sheet.getDataRange().getValues();
      var cleanNewName = name.toString().toLowerCase().replace(/[^a-z0-9]/g, '');

      for (var i = 1; i < data.length; i++) {
        var existingName = data[i][1];
        if (existingName) {
          var cleanExisting = existingName.toString().toLowerCase().replace(/[^a-z0-9]/g, '');
          if (cleanExisting === cleanNewName) {
            // It's already there! Don't add it.
            return ContentService.createTextOutput(JSON.stringify({'result': 'duplicate'}));
          }
        }
      }

      // 3. WRITE TO SHEET
      // Order: [Date, Name, Borough, Type, Courts]
      sheet.appendRow([new Date(), name, borough, type, courts]);
      
      return ContentService.createTextOutput(JSON.stringify({'result': 'success'}));
    }

  } catch (err) {
    // If something crashes, tell the map
    return ContentService.createTextOutput(JSON.stringify({'result': 'error', 'message': err.toString()}));
  } finally {
    lock.releaseLock();
  }
}

// ... YOUR NOTION CODE STARTS BELOW THIS LINE ...
// ==========================================
// 2. CONFIGURATION
// ==========================================
// ⚠️ PASTE YOUR NEW TOKEN HERE (NOT THE OLD ONE)
const NOTION_TOKEN = “YOUR”_NOTION_TOKEN; 
const DATABASE_ID = "2bd5c6af88da818eb2e2f78b6ec54b9d";

// HEADERS (Matches your Google Sheet)
const COL_SITE_NAME = "Type Name";       // Column B
const COL_BOROUGH = "Borough";           // Column C
const COL_GPS = "Geo Coordinates";       // Column G
const COL_STATUS = "Status";             // Column F
const COL_SYNCED = "Synced";             // Column H

// NOTION PROPERTIES
const NOTION_PROP_NAME = "Site Name";          
const NOTION_PROP_PARENT = "Parent Park";      
const NOTION_PROP_GPS = "GPS Coordinates ";    
const NOTION_PROP_STATUS = "Status";

// ==========================================
// 📍 BUTTON 1: GET LONDON GPS
// ==========================================
function fillMissingGPS() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = sheet.getDataRange().getValues();
  
  // Clean headers (Trim spaces)
  const headers = data[0].map(h => h.toString().trim()); 

  const nameIdx = headers.indexOf(COL_SITE_NAME);
  const boroughIdx = headers.indexOf(COL_BOROUGH);
  const gpsIdx = headers.indexOf(COL_GPS);

  if (nameIdx === -1 || gpsIdx === -1) {
    SpreadsheetApp.getUi().alert(`Error: Can't find columns. Looking for "${COL_SITE_NAME}" and "${COL_GPS}"`);
    return;
  }

  let updateCount = 0;
  
  for (let i = 1; i < data.length; i++) {
    const siteName = data[i][nameIdx];
    const borough = boroughIdx > -1 ? data[i][boroughIdx] : "";
    const currentGPS = data[i][gpsIdx];

    // SKIP IF: Name is empty, "nan", or GPS exists
    if (!siteName || String(siteName).toLowerCase() === "nan" || currentGPS !== "") continue;
    if (String(currentGPS).includes("#NAME")) continue; 

    // 🔍 CHANGE 1: Force search in London
    const query = `${siteName}, ${borough}, London, United Kingdom`;
    
    try {
      const geocoder = Maps.newGeocoder().setRegion('uk');
      const response = geocoder.geocode(query);
      
      if (response.status === 'OK' && response.results.length > 0) {
        const loc = response.results[0].geometry.location;
        const lat = loc.lat;
        const lng = loc.lng;

        // 🔍 CHANGE 2: London Bounding Box Check
        // (Roughly: Lat 51.2 to 51.7, Lon -0.6 to 0.4)
        if (lat > 51.2 && lat < 51.8 && lng > -0.6 && lng < 0.4) {
           const coords = `(${lat}, ${lng})`;
           sheet.getRange(i + 1, gpsIdx + 1).setValue(coords);
           updateCount++;
           Utilities.sleep(400); 
        } else {
           console.log(`Skipped ${siteName} - Coordinates (${lat},${lng}) are outside London.`);
        }
      }
    } catch (e) {
      console.log("GPS Error on row " + i + ": " + e.toString());
    }
  }
  
  SpreadsheetApp.getUi().alert(`✅ London GPS found for ${updateCount} parks.`);
}

// ==========================================
// 🚀 BUTTON 2: PUSH TO NOTION
// ==========================================
function pushToNotion() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = sheet.getDataRange().getValues();
  const headers = data[0].map(h => h.toString().trim()); 

  const syncedIdx = headers.indexOf(COL_SYNCED);
  const nameIdx = headers.indexOf(COL_SITE_NAME);
  const gpsIdx = headers.indexOf(COL_GPS);
  const statusIdx = headers.indexOf(COL_STATUS);

  if (syncedIdx === -1) {
    SpreadsheetApp.getUi().alert(`Error: Please add a column named '${COL_SYNCED}'`);
    return;
  }

  let successCount = 0;

  for (let i = 1; i < data.length; i++) {
    const row = data[i];
    const siteName = row[nameIdx];
    
    // FILTER: Skip if Synced, Empty Name, or "nan"
    if (row[syncedIdx] === "Yes" || !siteName) continue;
    if (String(siteName).toLowerCase() === "nan") continue;

    try {
      const properties = {};

      properties[NOTION_PROP_NAME] = { title: [{ text: { content: String(siteName) } }] };
      properties[NOTION_PROP_PARENT] = { rich_text: [{ text: { content: String(siteName) } }] };

      if (gpsIdx > -1 && row[gpsIdx] && !String(row[gpsIdx]).includes("#")) {
        properties[NOTION_PROP_GPS] = { rich_text: [{ text: { content: String(row[gpsIdx]) } }] };
      }

      if (statusIdx > -1 && row[statusIdx]) {
        properties[NOTION_PROP_STATUS] = { select: { name: String(row[statusIdx]) } };
      }

      const url = "https://api.notion.com/v1/pages";
      const options = {
        method: "post",
        headers: {
          "Authorization": `Bearer ${NOTION_TOKEN}`,
          "Notion-Version": "2022-06-28",
          "Content-Type": "application/json"
        },
        payload: JSON.stringify({
          parent: { database_id: DATABASE_ID },
          properties: properties
        }),
        muteHttpExceptions: true
      };

      const response = UrlFetchApp.fetch(url, options);
      
      if (response.getResponseCode() === 200) {
        sheet.getRange(i + 1, syncedIdx + 1).setValue("Yes"); 
        successCount++;
      } else {
        console.log(`Failed Row ${i+1}: ${response.getContentText()}`);
      }

    } catch (e) {
      console.log(`Error Row ${i+1}: ${e.message}`);
    }
  }
  
  if (successCount > 0) {
    SpreadsheetApp.getUi().alert(`🎉 Synced ${successCount} parks to Notion!`);
  } else {
    SpreadsheetApp.getUi().alert("No new valid rows found to sync.");
  }
}

function onOpen() {
  SpreadsheetApp.getUi().createMenu('🌟 Notion Sync')
      .addItem('1. Auto-Fill GPS (London)', 'fillMissingGPS')
      .addItem('2. Push to Notion', 'pushToNotion')
      .addSeparator()
      .addItem('3. Cleanup Duplicates', 'cleanupDuplicates')
      .addToUi();
}

// ==========================================
// 🧹 BUTTON 3: CLEANUP DUPLICATES (Parent Park Logic)
// ==========================================
function cleanupDuplicates() {
  const ui = SpreadsheetApp.getUi();
  
  // 1. Fetch ALL pages from Notion
  let allPages = [];
  let hasMore = true;
  let startCursor = undefined;
  
  ui.alert("⏳ Scanning Notion database by Parent Park... This might take a moment.");

  while (hasMore) {
    const url = `https://api.notion.com/v1/databases/${DATABASE_ID}/query`;
    const payload = { page_size: 100 };
    if (startCursor) payload.start_cursor = startCursor;

    const options = {
      method: "post",
      headers: {
        "Authorization": `Bearer ${NOTION_TOKEN}`,
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
      },
      payload: JSON.stringify(payload),
      muteHttpExceptions: true
    };

    const response = UrlFetchApp.fetch(url, options);
    const data = JSON.parse(response.getContentText());
    
    if (data.results) {
      allPages = allPages.concat(data.results);
    }
    
    hasMore = data.has_more;
    startCursor = data.next_cursor;
  }

  // 2. Group pages strictly by "Parent Park"
  const parkMap = {};
  
  allPages.forEach(page => {
    let parentParkValue = "";
    
    // EXTRACT PARENT PARK (Rich Text)
    if (page.properties[NOTION_PROP_PARENT] && page.properties[NOTION_PROP_PARENT].rich_text.length > 0) {
      parentParkValue = page.properties[NOTION_PROP_PARENT].rich_text[0].plain_text;
    }
    
    // EXTRACT STATUS (Select)
    let status = "";
    if (page.properties[NOTION_PROP_STATUS] && page.properties[NOTION_PROP_STATUS].select) {
      status = page.properties[NOTION_PROP_STATUS].select.name;
    }

    if (parentParkValue) {
      // Clean up the name (lowercase/trim) to catch "Hyde Park" vs "hyde park"
      const cleanParent = parentParkValue.toLowerCase().trim();

      if (!parkMap[cleanParent]) parkMap[cleanParent] = [];
      
      // Add this row to the Parent Park bucket
      parkMap[cleanParent].push({ 
        id: page.id, 
        status: status, 
        originalName: parentParkValue 
      });
    }
  });

  // 3. Logic: Compare rows INSIDE each Parent Park bucket
  let pagesToDelete = [];

  for (const [parentName, rows] of Object.entries(parkMap)) {
    // We only care if this Parent Park has multiple entries
    if (rows.length > 1) {
      
      // A. Does this Parent Park have a "Surveyed" row?
      const hasSurveyed = rows.some(r => {
        const s = String(r.status).toLowerCase();
        return s === "surveyed" || s === "completed" || s === "done";
      });
      
      // B. Filter the "Awaiting" rows
      const awaitingRows = rows.filter(r => {
        const s = String(r.status).toLowerCase();
        return s === "awaiting survey" || s === "awaiting";
      });

      // --- RULE 1: If 'Surveyed' exists, delete ALL 'Awaiting Survey' rows ---
      if (hasSurveyed && awaitingRows.length > 0) {
        awaitingRows.forEach(r => {
          pagesToDelete.push({ id: r.id, name: r.originalName, reason: "Already Surveyed" });
        });
      }
      
      // --- RULE 2: If NO 'Surveyed' exists, but multiple 'Awaiting', delete duplicates (Keep 1) ---
      else if (!hasSurveyed && awaitingRows.length > 1) {
        // We start loop at i=1 (Index 1) to SKIP the first one (Index 0).
        // Index 0 is kept safe. Index 1, 2, 3... are marked for death.
        for (let i = 1; i < awaitingRows.length; i++) {
          pagesToDelete.push({ 
            id: awaitingRows[i].id, 
            name: awaitingRows[i].originalName,
            reason: "Duplicate Awaiting"
          });
        }
      }
    }
  }

  if (pagesToDelete.length === 0) {
    ui.alert("✅ No duplicates found.");
    return;
  }

  // 4. Confirm Deletion
  const confirm = ui.alert(
    `⚠️ Found ${pagesToDelete.length} rows to delete.\n\n` + 
    `Reasons:\n` +
    `1. 'Surveyed' exists elsewhere (Rule 1)\n` +
    `2. Double 'Awaiting Survey' entries (Rule 2)\n\n` +
    `Example: '${pagesToDelete[0].name}'\n\nProceed?`,
    ui.ButtonSet.YES_NO
  );

  if (confirm !== ui.Button.YES) return;

  let deletedCount = 0;

  pagesToDelete.forEach((p, index) => {
    try {
      const delUrl = `https://api.notion.com/v1/pages/${p.id}`;
      const delOptions = {
        method: "patch",
        headers: {
          "Authorization": `Bearer ${NOTION_TOKEN}`,
          "Notion-Version": "2022-06-28",
          "Content-Type": "application/json"
        },
        payload: JSON.stringify({ archived: true }),
        muteHttpExceptions: true
      };
      
      UrlFetchApp.fetch(delUrl, delOptions);
      deletedCount++;
      
      if (index % 5 === 0) Utilities.sleep(200); 
    } catch (e) {
      console.log(`Failed to delete row for ${p.name}`);
    }
  });

  ui.alert(`🧹 Cleaned up ${deletedCount} duplicate rows.`);
}
