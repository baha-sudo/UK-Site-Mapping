# @title 🇬🇧 UK Dashboard (Optimized Route + Sports Info Fixed)
from IPython.display import display, HTML
from google.colab import files
import time

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
# ⚠️ USE A NEW TOKEN HERE
NOTION_TOKEN = “YOUR _NOTION_TOKEN”
DATABASE_ID = "2bd5c6af88da818eb2e2f78b6ec54b9d"

print("⏳ Generating Dashboard...")

# ==========================================
# THE APP CODE
# ==========================================
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>UK Installation Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; padding: 0; font-family: 'Inter', sans-serif; overflow: hidden; }
        #map { height: 100vh; width: 100%; z-index: 1; }

        .control-panel {
            position: absolute; top: 20px; right: 20px; width: 340px;
            background: rgba(255, 255, 255, 0.95);
            padding: 24px; border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
            z-index: 1000; backdrop-filter: blur(10px);
            max-height: 90vh; overflow-y: auto;
            border: 1px solid rgba(255,255,255,0.5);
        }

        h2 { margin: 0 0 8px 0; font-size: 20px; color: #0f172a; font-weight: 700; }
        p { font-size: 13px; color: #64748b; margin-bottom: 20px; }

        .btn-group { display: flex; gap: 12px; margin-bottom: 20px; }
        .action-btn { flex: 1; padding: 12px; border: none; border-radius: 10px; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: transform 0.1s; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .action-btn:active { transform: scale(0.98); }
        .btn-sync { background-color: #2563eb; color: white; }
        .btn-sync:hover { background-color: #1d4ed8; }
        .btn-route { background-color: #10b981; color: white; }
        .btn-route:hover { background-color: #059669; }
        .btn-cancel { background-color: #ef4444; color: white; width:100%; margin-top:10px;}

        /* Route Planner Styles */
        .route-section { background: #f0fdf4; border: 1px solid #86efac; border-radius: 12px; padding: 15px; margin-bottom: 20px; display: none; }
        .route-header { font-size: 14px; font-weight: 700; color: #15803d; margin-bottom: 10px; display:flex; justify-content:space-between; align-items:center;}

        .step-box { background: white; border: 1px solid #bbf7d0; padding: 12px; border-radius: 8px; margin-bottom: 10px; }
        .step-title { font-size: 11px; text-transform: uppercase; color: #15803d; font-weight: 700; margin-bottom: 5px; letter-spacing: 0.5px; }
        .step-val { font-size: 13px; color: #111; font-weight: 600; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }

        .route-status { font-size: 12px; color: #166534; margin-bottom: 10px; font-weight: 600; text-align: center; }
        .route-link-btn { width: 100%; background: #0f172a; color: white; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; display: none; font-size: 13px; font-weight: bold; cursor: pointer; margin-top: 10px;}
        .route-link-btn:hover { background: #334155; }

        /* Filters */
        .filter-section { border-top: 1px solid #e2e8f0; padding-top: 20px; }
        .filter-title { font-size: 11px; font-weight: 700; color: #94a3b8; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px; }
        .toggle-container { display: flex; flex-direction: column; gap: 8px; }
        .filter-toggle { display: flex; align-items: center; justify-content: space-between; padding: 10px 14px; background: #f8fafc; border-radius: 8px; font-size: 13px; color: #475569; cursor: pointer; user-select: none; border: 1px solid transparent; transition: all 0.2s; }
        .filter-toggle:hover { background: #f1f5f9; }
        .filter-toggle.active { background: #fff; border-color: #cbd5e1; color: #0f172a; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
        .filter-toggle .count { font-size: 11px; background: #e2e8f0; padding: 2px 6px; border-radius: 10px; color: #64748b; }

        /* Popups */
        .popup-content { width: 260px; font-family: 'Inter', sans-serif; }
        .popup-header { font-size: 16px; font-weight: 700; margin-bottom: 12px; color: #0f172a; border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; }
        .popup-row { display: flex; justify-content: space-between; margin: 6px 0; font-size: 13px; align-items: center; }
        .popup-label { color: #64748b; font-size: 12px; }
        .popup-val { font-weight: 600; color: #334155; text-align: right; }
        .status-badge { background: #eff6ff; color: #2563eb; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; text-transform: uppercase; }
        .popup-sports { margin-top: 15px; background: #f8fafc; padding: 10px; border-radius: 8px; font-size: 12px; text-align: center; border: 1px solid #e2e8f0; }
        .popup-link { display: block; margin-top: 12px; text-align: center; background: #0f172a; color: white; text-decoration: none; padding: 10px; border-radius: 8px; font-size: 12px; font-weight: 600; }

        .spinner { width: 14px; height: 14px; border: 2px solid #fff; border-bottom-color: transparent; border-radius: 50%; animation: rot 1s linear infinite; display: none; }
        @keyframes rot { 100% { transform: rotate(360deg); } }
        #log { font-size: 12px; color: #ef4444; margin-top: 15px; text-align: center; background: #fef2f2; padding: 8px; border-radius: 6px; display:none; }
    </style>
</head>
<body>
    <div id="map"></div>
    <div class="control-panel">
        <h2>Site Operations Map</h2>
        <p>Sync data & Plan Optimized Routes.</p>

        <div class="btn-group">
            <button class="action-btn btn-sync" onclick="syncNotion()">
                <span class="spinner" id="loader"></span>
                <span id="btn-text">Sync Data</span>
            </button>
            <button class="action-btn btn-route" onclick="toggleRouteUI()" id="btn-planner">
                🚴 Plan Cycle Route
            </button>
        </div>

        <div class="route-section" id="route-ui">
            <div class="route-header">
                Route Optimizer (BETA)
                <span style="font-size:16px; cursor:pointer;" onclick="toggleRouteUI()">×</span>
            </div>

            <div class="step-box" id="step-1-box" style="border-color:#3b82f6; background:#eff6ff; cursor:pointer;" onclick="setMode('start')">
                <div class="step-title" style="color:#2563eb">1. Start Point</div>
                <div class="step-val" id="start-val">Click here or pick on map...</div>
            </div>

            <div class="step-box" id="step-2-box" onclick="setMode('destinations')">
                <div class="step-title">2. Select Sites</div>
                <div class="step-val" id="sites-val">0 Selected</div>
            </div>

            <div class="route-status" id="route-status">Select a Start Point first.</div>

            <a id="maps-link" class="route-link-btn" target="_blank">🚀 Open Optimized Route</a>
            <button class="action-btn btn-cancel" onclick="resetRoute()">Reset</button>
        </div>

        <div class="filter-section">
            <div class="filter-title">Filter by Approval</div>
            <div class="toggle-container" id="filter-container">
                <div style="font-size:12px; color:#94a3b8; text-align:center; padding:15px;">Click "Sync Data" to load filters...</div>
            </div>
        </div>
        <div id="log"></div>
    </div>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        const NOTION_TOKEN = "REPLACE_TOKEN";
        const DATABASE_ID = "REPLACE_ID";
        const map = L.map('map').setView([54.5, -3.0], 6);
        L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', { attribution: 'CARTO', maxZoom: 19 }).addTo(map);

        let allData = [];
        let markersLayer = L.layerGroup().addTo(map);
        let activeFilters = new Set();
        let markerMap = new Map();

        // Route State
        let routeMode = 'none'; // 'start', 'destinations', 'none'
        let startPoint = null;
        let selectedSites = [];

        const emojiMap = { "Football": "⚽", "Soccer": "⚽", "Basketball": "🏀", "Tennis": "🎾", "Baseball": "⚾", "Cricket": "🏏", "Rugby": "🏉", "Volleyball": "🏐", "Running": "🏃", "Playground": "🛝", "Gym": "🏋️", "Swimming": "🏊" };

        function getEmoji(text) { if (!text) return ""; for (let [key, icon] of Object.entries(emojiMap)) { if (text.toLowerCase().includes(key.toLowerCase())) return icon; } return "📍"; }

        function getColor(approval) {
            if (!approval) return "#64748b";
            const app = approval.toLowerCase();
            if (app.includes("not") || app.includes("no") || app.includes("reject") || app.includes("decline")) return "#ef4444";
            if (app.includes("approved") || app.includes("yes")) return "#10b981";
            if (app.includes("wait") || app.includes("pending")) return "#f59e0b";
            if (app.includes("revisit")) return "#8b5cf6";
            return "#3b82f6";
        }

        // Icons
        function createIcon(color) { return L.divIcon({ className: 'custom-pin', html: `<svg viewBox="0 0 24 24" fill="${color}" width="45" height="45" style="filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3));"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/><circle cx="12" cy="9" r="2.5" fill="white"/></svg>`, iconSize: [45, 45], iconAnchor: [22.5, 45], popupAnchor: [0, -45] }); }

        function createStartIcon() { return L.divIcon({ className: 'start-pin', html: `<svg viewBox="0 0 24 24" fill="#2563eb" width="50" height="50" style="filter: drop-shadow(0 0 10px rgba(37, 99, 235, 0.6));"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/><text x="12" y="14" font-size="10" text-anchor="middle" fill="white" font-weight="bold">START</text></svg>`, iconSize: [50, 50], iconAnchor: [25, 50], popupAnchor: [0, -50] }); }

        function createSelectedIcon(num) { return L.divIcon({ className: 'selected-pin', html: `<svg viewBox="0 0 24 24" fill="#fbbf24" width="50" height="50" style="filter: drop-shadow(0 0 10px rgba(251, 191, 36, 0.8));"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/><text x="12" y="14" font-size="10" text-anchor="middle" fill="black" font-weight="bold">${num}</text></svg>`, iconSize: [50, 50], iconAnchor: [25, 50], popupAnchor: [0, -50] }); }

        // --- ROUTE PLANNER LOGIC ---
        function toggleRouteUI() {
            const ui = document.getElementById('route-ui');
            if (ui.style.display === 'block') {
                ui.style.display = 'none';
                resetRoute();
            } else {
                ui.style.display = 'block';
                setMode('start');
            }
        }

        function setMode(mode) {
            routeMode = mode;
            if (mode === 'start') {
                document.getElementById('step-1-box').style.borderColor = "#3b82f6";
                document.getElementById('step-1-box').style.backgroundColor = "#eff6ff";
                document.getElementById('step-2-box').style.borderColor = "#bbf7d0";
                document.getElementById('step-2-box').style.backgroundColor = "white";
                document.getElementById('route-status').innerText = "Click a pin on the map to set START point.";
            } else if (mode === 'destinations') {
                if (!startPoint) { setMode('start'); return; }
                document.getElementById('step-1-box').style.borderColor = "#bbf7d0";
                document.getElementById('step-1-box').style.backgroundColor = "white";
                document.getElementById('step-2-box').style.borderColor = "#3b82f6";
                document.getElementById('step-2-box').style.backgroundColor = "#eff6ff";
                document.getElementById('route-status').innerText = "Now click sites to add to your route.";
            }
        }

        function resetRoute() {
            startPoint = null;
            selectedSites = [];
            routeMode = 'none';
            document.getElementById('start-val').innerText = "Click here or pick on map...";
            document.getElementById('sites-val').innerText = "0 Selected";
            document.getElementById('maps-link').style.display = 'none';
            document.getElementById('route-status').innerText = "";
            renderMap();
        }

        function handleMarkerClick(d, marker) {
            if (routeMode === 'none') return; // Standard popup

            marker.closePopup(); // Prevent default popup

            if (routeMode === 'start') {
                startPoint = d;
                document.getElementById('start-val').innerText = d.name;
                setMode('destinations');
                renderMap();
            } else if (routeMode === 'destinations') {
                if (startPoint && d.name === startPoint.name) return; // Can't visit start

                const idx = selectedSites.findIndex(site => site.name === d.name);
                if (idx > -1) {
                    selectedSites.splice(idx, 1); // Deselect
                } else {
                    if (selectedSites.length >= 23) { alert("Google Maps limit reached (23 stops)."); return; }
                    selectedSites.push(d);
                }
                document.getElementById('sites-val').innerText = `${selectedSites.length} Selected`;
                generateOptimizedLink();
                renderMap();
            }
        }

        // --- 🧠 INSANE OPTIMIZATION (Greedy Nearest Neighbor) ---
        function calculateOptimizedOrder() {
            if (!startPoint || selectedSites.length === 0) return [];

            let unvisited = [...selectedSites];
            let current = startPoint;
            let path = [];

            while (unvisited.length > 0) {
                let nearest = null;
                let minDist = Infinity;
                let nearestIdx = -1;

                for (let i = 0; i < unvisited.length; i++) {
                    const site = unvisited[i];
                    const dist = Math.sqrt(Math.pow(site.lat - current.lat, 2) + Math.pow(site.lng - current.lng, 2));
                    if (dist < minDist) {
                        minDist = dist;
                        nearest = site;
                        nearestIdx = i;
                    }
                }

                path.push(nearest);
                current = nearest;
                unvisited.splice(nearestIdx, 1);
            }
            return path;
        }

        function generateOptimizedLink() {
            if (!startPoint || selectedSites.length === 0) {
                document.getElementById('maps-link').style.display = 'none';
                return;
            }

            const optimizedSites = calculateOptimizedOrder();

            const origin = `&origin=${startPoint.lat},${startPoint.lng}`;
            const lastSite = optimizedSites[optimizedSites.length - 1];
            const destination = `&destination=${lastSite.lat},${lastSite.lng}`;

            let waypointsParam = "";
            if (optimizedSites.length > 1) {
                const intermediate = optimizedSites.slice(0, -1);
                waypointsParam = `&waypoints=${intermediate.map(s => `${s.lat},${s.lng}`).join('|')}`;
            }

            const finalUrl = `https://www.google.com/maps/dir/?api=1${origin}${destination}${waypointsParam}&travelmode=bicycling`;

            const linkBtn = document.getElementById('maps-link');
            linkBtn.href = finalUrl;
            linkBtn.style.display = 'block';

            document.getElementById('route-status').innerHTML = `✅ Route Optimized for <strong>${selectedSites.length}</strong> sites!`;
        }

        // --- NOTION SYNC & STANDARD MAP ---
        async function syncNotion() {
            const btn = document.querySelector('.btn-sync'); const loader = document.getElementById('loader'); const log = document.getElementById('log');
            btn.disabled = true; loader.style.display = 'block'; document.getElementById('btn-text').innerText = "Fetching..."; log.style.display = 'none';
            let accumulatedResults = []; let hasMore = true; let startCursor = undefined;
            try {
                while (hasMore) {
                    const proxyUrl = "https://corsproxy.io/?";
                    const targetUrl = `https://api.notion.com/v1/databases/${DATABASE_ID}/query`;
                    const payload = { page_size: 100 }; if (startCursor) payload.start_cursor = startCursor;
                    const response = await fetch(proxyUrl + encodeURIComponent(targetUrl), { method: 'POST', headers: { 'Authorization': `Bearer ${NOTION_TOKEN}`, 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
                    if (!response.ok) throw new Error(`Status: ${response.status}`);
                    const data = await response.json(); accumulatedResults = accumulatedResults.concat(data.results); hasMore = data.has_more; startCursor = data.next_cursor;
                    document.getElementById('btn-text').innerText = `Fetched ${accumulatedResults.length}...`;
                }
                allData = accumulatedResults.map(page => parsePage(page)).filter(item => item.lat !== null);
                generateFilters(allData); renderMap(); document.getElementById('btn-text').innerText = `Synced ${allData.length} Sites`;
            } catch (error) { console.error(error); log.style.display = 'block'; log.innerText = "Error: " + error.message; }
            finally { btn.disabled = false; loader.style.display = 'none'; }
        }

        function extractProp(props, name, type) { const prop = props[name]; if (!prop) return ""; try { if (type === 'title') return prop.title[0]?.plain_text || "Untitled"; if (type === 'rich_text') return prop.rich_text[0]?.plain_text || ""; if (type === 'select') return prop.select?.name || ""; if (type === 'status') return prop.status?.name || ""; if (type === 'number') return prop.number || 0; if (type === 'formula') return prop.formula.string || prop.formula.number || ""; } catch (e) { return ""; } return ""; }
        function parsePage(page) {
            const p = page.properties; const name = extractProp(p, 'Site Name', 'title');
            const gpsProp = p['GPS Coordinates ']; let gpsRaw = ""; if (gpsProp && gpsProp.rich_text.length > 0) gpsRaw = gpsProp.rich_text[0].plain_text;
            const matches = gpsRaw.match(/-?\\d+(\\.\\d+)?/g); let lat = null, lng = null; if (matches && matches.length >= 2) { lat = parseFloat(matches[0]); lng = parseFloat(matches[1]); }
            const status = extractProp(p, 'Status', 'select'); const approval = extractProp(p, 'Pre Installation Approval', 'select') || "Unspecified"; const score = extractProp(p, 'Site Score', 'formula'); const link = extractProp(p, 'Formula', 'formula');
            const sports = [extractProp(p, 'Compartment 1', 'select'), extractProp(p, 'Compartment 2', 'select'), extractProp(p, 'Compartment 3', 'select')].filter(Boolean).map(s => `${getEmoji(s)} ${s}`).join("  •  ");
            return { lat, lng, name, status, approval, score, link, sports };
        }
        function generateFilters(data) {
            const container = document.getElementById('filter-container'); container.innerHTML = "";
            const categories = [...new Set(data.map(d => d.approval))].sort(); activeFilters = new Set(categories);
            categories.forEach(cat => {
                const count = data.filter(d => d.approval === cat).length; const div = document.createElement('div'); div.className = 'filter-toggle active';
                const color = getColor(cat); div.innerHTML = `<div style="display:flex; align-items:center;"><span style="width:10px; height:10px; border-radius:50%; background:${color}; display:inline-block; margin-right:8px;"></span> ${cat}</div><span class="count">${count}</span>`;
                div.onclick = () => { if (activeFilters.has(cat)) { activeFilters.delete(cat); div.classList.remove('active'); div.style.opacity = "0.6"; } else { activeFilters.add(cat); div.classList.add('active'); div.style.opacity = "1"; } renderMap(); }; container.appendChild(div);
            });
        }
        function renderMap() {
            markersLayer.clearLayers(); const bounds = []; markerMap.clear();
            allData.forEach(d => {
                if (!activeFilters.has(d.approval)) return;

                let icon;
                if (startPoint && d.name === startPoint.name) {
                    icon = createStartIcon();
                } else {
                    const isSelected = selectedSites.findIndex(s => s.name === d.name);
                    icon = (isSelected > -1) ? createSelectedIcon(isSelected + 1) : createIcon(getColor(d.approval));
                }

                const marker = L.marker([d.lat, d.lng], { icon: icon });

                // --- SPORTS INFO ADDED BACK HERE ---
                const popupHtml = `<div class="popup-content"><div class="popup-header">${d.name}</div><div class="popup-row"><span class="popup-label">Approval</span> <span class="popup-val" style="color:${getColor(d.approval)}">${d.approval}</span></div><div class="popup-row"><span class="popup-label">Current Status</span> <span class="status-badge">${d.status || "N/A"}</span></div><div class="popup-sports">${d.sports || "No sports info"}</div><a href="${d.link}" target="_blank" class="popup-link">Show More Details ↗</a></div>`;

                marker.bindPopup(popupHtml);
                marker.on('click', () => handleMarkerClick(d, marker));
                markersLayer.addLayer(marker); bounds.push([d.lat, d.lng]);
            });
            if (bounds.length > 0 && routeMode === 'none') map.fitBounds(bounds, { padding: [50, 50] });
        }
    </script>
</body>
</html>
"""

final_html = html_code.replace("REPLACE_TOKEN", NOTION_TOKEN).replace("REPLACE_ID", DATABASE_ID)
with open('UK_Site_Map_Final.html', 'w') as f: f.write(final_html)
files.download('UK_Site_Map_Final.html')
print("✅ Done! Downloaded UK_Site_Map_Final.html")
