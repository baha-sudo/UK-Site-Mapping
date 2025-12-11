{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red113\green171\blue89;\red30\green31\blue33;\red202\green202\blue202;
\red188\green135\blue186;\red212\green214\blue154;\red212\green212\blue212;\red194\green126\blue101;\red113\green184\blue255;
\red88\green147\blue206;\red67\green192\blue160;\red140\green211\blue254;\red167\green197\blue152;\red70\green137\blue204;
}
{\*\expandedcolortbl;;\cssrgb\c50980\c71765\c42353;\cssrgb\c15686\c16471\c17255;\cssrgb\c83137\c83137\c83137;
\cssrgb\c78824\c61176\c77647;\cssrgb\c86275\c86275\c66667;\cssrgb\c86275\c86275\c86275;\cssrgb\c80784\c56863\c47059;\cssrgb\c50980\c77647\c100000;
\cssrgb\c41176\c64706\c84314;\cssrgb\c30588\c78824\c69020;\cssrgb\c61176\c86275\c99608;\cssrgb\c70980\c80784\c65882;\cssrgb\c33725\c61176\c83922;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww28900\viewh17540\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # ==============================================================================\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u55357 \u57000  INSTRUCTIONS FOR THE RECIPIENT \u55357 \u57000 \cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # ==============================================================================\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # 1. Create a folder in your Google Drive named: "LondonMapData"\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # 2. Upload the following two files into that folder:\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #    - london_parks_master.gpkg\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #    - london_boroughs_master.gpkg\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # 3. Run this cell. It will install dependencies, ask for Drive permission,\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #    process the data, and download the final HTML map to your computer.\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # ==============================================================================\cf4 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 # --- 1. INSTALL DEPENDENCIES ---\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 import\cf4 \strokec4  subprocess\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  sys\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf7 \strokec7 (\cf8 \strokec8 "\uc0\u9203  Installing dependencies... (this may take a minute)"\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 subprocess.check_call\cf7 \strokec7 ([\cf4 \strokec4 sys.executable\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "-m"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "pip"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "install"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "geopandas"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "folium"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "matplotlib"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "mapclassify"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "osmnx"\cf7 \strokec7 ])\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf7 \strokec7 (\cf8 \strokec8 "\uc0\u9989  Dependencies installed."\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- 2. MOUNT GOOGLE DRIVE ---\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 from\cf4 \strokec4  google.colab \cf5 \strokec5 import\cf4 \strokec4  drive\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  os\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf7 \strokec7 (\cf8 \strokec8 "\uc0\u55357 \u56514  Mounting Google Drive..."\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf9 \cb3 \strokec9 not\cf4 \cb3 \strokec4  os.path.exists\cf7 \strokec7 (\cf8 \strokec8 '/content/drive'\cf7 \strokec7 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     drive.mount\cf7 \strokec7 (\cf8 \strokec8 '/content/drive'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- 3. MAIN SCRIPT ---\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # SCRIPT 2: LOCATION IDENTIFIER v41.0 (Logic Overhaul)\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # ==========================================\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 import\cf4 \strokec4  geopandas \cf5 \strokec5 as\cf4 \strokec4  gpd\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  folium\cb1 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  folium.plugins \cf5 \strokec5 import\cf4 \strokec4  Fullscreen\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  pandas \cf5 \strokec5 as\cf4 \strokec4  pd\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  hashlib\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # import webbrowser  <-- Removed for Colab compatibility\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 from\cf4 \strokec4  google.colab \cf5 \strokec5 import\cf4 \strokec4  files \cf2 \strokec2 # Added for Colab download\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  matplotlib.pyplot \cf5 \strokec5 as\cf4 \strokec4  plt\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  matplotlib.colors \cf5 \strokec5 as\cf4 \strokec4  colors\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  json\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  osmnx \cf5 \strokec5 as\cf4 \strokec4  ox\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- CONFIGURATION ---\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 GOOGLE_SCRIPT_URL = \cf8 \strokec8 "hhttps://script.google.com/macros/s/AKfycbwROIHUvDeLoxdWJDWl_zZ5H9aMi4xypvfKbToH4ozGhHqBGD_XA6SSDmI4GcXFlGAh/exec"\cf4 \cb1 \strokec4 \
\cb3 DATA_DIR = \cf8 \strokec8 "/content/drive/MyDrive/LondonMapData"\cf4 \cb1 \strokec4 \
\cb3 parks_file = \cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 "\cf7 \strokec7 \{\cf4 \strokec4 DATA_DIR\cf7 \strokec7 \}\cf8 \strokec8 /london_parks_master.gpkg"\cf4 \cb1 \strokec4 \
\cb3 boroughs_file = \cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 "\cf7 \strokec7 \{\cf4 \strokec4 DATA_DIR\cf7 \strokec7 \}\cf8 \strokec8 /london_boroughs_master.gpkg"\cf4 \cb1 \strokec4 \
\
\cb3 OFFICIAL_BOROUGHS = \cf7 \strokec7 [\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 "Barking and Dagenham"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Barnet"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Bexley"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Brent"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Bromley"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Camden"\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 "City of London"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Croydon"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Ealing"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Enfield"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Greenwich"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Hackney"\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 "Hammersmith and Fulham"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Haringey"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Harrow"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Havering"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Hillingdon"\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 "Hounslow"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Islington"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Kensington and Chelsea"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Kingston upon Thames"\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 "Lambeth"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Lewisham"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Merton"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Newham"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Redbridge"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Richmond upon Thames"\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 "Southwark"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Sutton"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Tower Hamlets"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Waltham Forest"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Wandsworth"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "Westminster"\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 ]\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf7 \strokec7 (\cf8 \strokec8 "\uc0\u55357 \u56960  Starting Logic Overhaul Dashboard v41.0..."\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cf6 \cb3 \strokec6 print\cf7 \strokec7 (\cf8 \strokec8 "\uc0\u55357 \u56514  Loading data..."\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # 1. LOAD DATA\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 try\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     gdf = gpd.read_file\cf7 \strokec7 (\cf4 \strokec4 parks_file\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3     boroughs_gdf = gpd.read_file\cf7 \strokec7 (\cf4 \strokec4 boroughs_file\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 print\cf7 \strokec7 (\cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 "   \uc0\u9989  Loaded raw data: \cf7 \strokec7 \{\cf6 \strokec6 len\cf7 \strokec7 (\cf4 \strokec4 gdf\cf7 \strokec7 )\}\cf8 \strokec8  features."\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 except\cf4 \strokec4  Exception \cf5 \strokec5 as\cf4 \strokec4  e\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 \strokec6 print\cf7 \strokec7 (\cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 "\uc0\u10060  Error: Files not found in \cf7 \strokec7 \{\cf4 \strokec4 DATA_DIR\cf7 \strokec7 \}\cf8 \strokec8 .\\n\cf7 \strokec7 \{\cf4 \strokec4 e\cf7 \strokec7 \}\cf8 \strokec8 "\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3     sys.\cf6 \strokec6 exit\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # 2. FILTERING\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 gdf = gdf.to_crs\cf7 \strokec7 (\cf8 \strokec8 "EPSG:3857"\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 gdf\cf7 \strokec7 [\cf8 \strokec8 'area_sqm'\cf7 \strokec7 ]\cf4 \strokec4  = gdf.geometry.area\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # A. BLACKLIST\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf8 \strokec8 'landuse'\cf4 \strokec4  \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  gdf.columns\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     gdf = gdf\cf7 \strokec7 [\cf4 \strokec4 ~gdf\cf7 \strokec7 [\cf8 \strokec8 'landuse'\cf7 \strokec7 ]\cf4 \strokec4 .astype\cf7 \strokec7 (\cf11 \cb3 \strokec11 str\cf7 \cb3 \strokec7 )\cf4 \strokec4 .isin\cf7 \strokec7 ([\cf8 \strokec8 'cemetery'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'religious'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'consecrated_ground'\cf7 \strokec7 ])]\cf4 \strokec4 .copy\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf8 \strokec8 'amenity'\cf4 \strokec4  \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  gdf.columns\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     gdf = gdf\cf7 \strokec7 [\cf4 \strokec4 ~gdf\cf7 \strokec7 [\cf8 \strokec8 'amenity'\cf7 \strokec7 ]\cf4 \strokec4 .astype\cf7 \strokec7 (\cf11 \cb3 \strokec11 str\cf7 \cb3 \strokec7 )\cf4 \strokec4 .isin\cf7 \strokec7 ([\cf8 \strokec8 'grave_yard'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'crematorium'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'place_of_worship'\cf7 \strokec7 ])]\cf4 \strokec4 .copy\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf8 \strokec8 'historic'\cf4 \strokec4  \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  gdf.columns\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     gdf = gdf\cf7 \strokec7 [\cf4 \strokec4 ~gdf\cf7 \strokec7 [\cf8 \strokec8 'historic'\cf7 \strokec7 ]\cf4 \strokec4 .astype\cf7 \strokec7 (\cf11 \cb3 \strokec11 str\cf7 \cb3 \strokec7 )\cf4 \strokec4 .isin\cf7 \strokec7 ([\cf8 \strokec8 'memorial'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'monument'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'cemetery'\cf7 \strokec7 ])]\cf4 \strokec4 .copy\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # B. AMENITIES\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 amenity_mask = \cf7 \strokec7 (\cf4 \cb1 \strokec4 \
\cb3     gdf\cf7 \strokec7 [\cf8 \strokec8 'leisure'\cf7 \strokec7 ]\cf4 \strokec4 .isin\cf7 \strokec7 ([\cf8 \strokec8 'pitch'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'track'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'fitness_station'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'playground'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'golf_course'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'sports_centre'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'muga'\cf7 \strokec7 ])\cf4 \strokec4  |\cb1 \
\cb3     gdf\cf7 \strokec7 [\cf8 \strokec8 'sport'\cf7 \strokec7 ]\cf4 \strokec4 .notna\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 amenities = gdf\cf7 \strokec7 [\cf4 \strokec4 amenity_mask\cf7 \strokec7 ]\cf4 \strokec4 .copy\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 def\cf4 \cb3 \strokec4  \cf6 \strokec6 categorize_amenity\cf4 \strokec4 (\cf12 \cb3 \strokec12 row\cf4 \cb3 \strokec4 )\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     leisure = \cf11 \cb3 \strokec11 str\cf7 \cb3 \strokec7 (\cf4 \strokec4 row\cf7 \strokec7 [\cf8 \strokec8 'leisure'\cf7 \strokec7 ])\cf4 \cb1 \strokec4 \
\cb3     sport = \cf11 \cb3 \strokec11 str\cf7 \cb3 \strokec7 (\cf4 \strokec4 row\cf7 \strokec7 [\cf8 \strokec8 'sport'\cf7 \strokec7 ])\cf4 \strokec4 .lower\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 if\cf4 \strokec4  leisure == \cf8 \strokec8 'playground'\cf7 \strokec7 :\cf4 \strokec4  \cf5 \strokec5 return\cf4 \strokec4  \cf8 \strokec8 'Playgrounds'\cf4 \cb1 \strokec4 \
\cb3     court_sports = \cf7 \strokec7 [\cf8 \strokec8 'tennis'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'basketball'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'netball'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'volleyball'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'pickleball'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'soccer'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'football'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'cricket'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'rugby'\cf7 \strokec7 ]\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 if\cf4 \strokec4  \cf6 \strokec6 any\cf7 \strokec7 (\cf4 \strokec4 s \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  sport \cf5 \strokec5 for\cf4 \strokec4  s \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  court_sports\cf7 \strokec7 ):\cf4 \strokec4  \cf5 \strokec5 return\cf4 \strokec4  \cf8 \strokec8 'Courts'\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 if\cf4 \strokec4  leisure \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  \cf7 \strokec7 [\cf8 \strokec8 'pitch'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'track'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'sports_centre'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'golf_course'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'muga'\cf7 \strokec7 ]:\cf4 \strokec4  \cf5 \strokec5 return\cf4 \strokec4  \cf8 \strokec8 'Courts'\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 return\cf4 \strokec4  \cf8 \strokec8 'Other'\cf4 \cb1 \strokec4 \
\
\cb3 amenities\cf7 \strokec7 [\cf8 \strokec8 'amenity_category'\cf7 \strokec7 ]\cf4 \strokec4  = amenities.apply\cf7 \strokec7 (\cf4 \strokec4 categorize_amenity\cf7 \strokec7 ,\cf4 \strokec4  axis=\cf13 \cb3 \strokec13 1\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # C. SITES (Size Filter > 2000sqm)\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 site_mask = \cf7 \strokec7 (\cf4 \cb1 \strokec4 \
\cb3     gdf\cf7 \strokec7 [\cf8 \strokec8 'leisure'\cf7 \strokec7 ]\cf4 \strokec4 .isin\cf7 \strokec7 ([\cf8 \strokec8 'park'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'recreation_ground'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'common'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'nature_reserve'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'garden'\cf7 \strokec7 ])\cf4 \strokec4  |\cb1 \
\cb3     gdf\cf7 \strokec7 [\cf8 \strokec8 'landuse'\cf7 \strokec7 ]\cf4 \strokec4 .isin\cf7 \strokec7 ([\cf8 \strokec8 'recreation_ground'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'village_green'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'forest'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'meadow'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'greenfield'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'grass'\cf7 \strokec7 ])\cf4 \strokec4  |\cb1 \
\cb3     \cf7 \strokec7 (\cf4 \strokec4 gdf\cf7 \strokec7 [\cf8 \strokec8 'natural'\cf7 \strokec7 ]\cf4 \strokec4 .isin\cf7 \strokec7 ([\cf8 \strokec8 'wood'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'heath'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'scrub'\cf7 \strokec7 ])\cf4 \strokec4  & \cf7 \strokec7 (\cf4 \strokec4 gdf\cf7 \strokec7 [\cf8 \strokec8 'area_sqm'\cf7 \strokec7 ]\cf4 \strokec4  > \cf13 \cb3 \strokec13 5000\cf7 \cb3 \strokec7 ))\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 containers = gdf\cf7 \strokec7 [\cf4 \strokec4 site_mask\cf7 \strokec7 ]\cf4 \strokec4 .copy\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\cb3 containers = containers\cf7 \strokec7 [\cf4 \strokec4 containers\cf7 \strokec7 [\cf8 \strokec8 'area_sqm'\cf7 \strokec7 ]\cf4 \strokec4  > \cf13 \cb3 \strokec13 2000\cf7 \cb3 \strokec7 ]\cf4 \strokec4 .copy\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\cb3 containers\cf7 \strokec7 [\cf8 \strokec8 'geometry'\cf7 \strokec7 ]\cf4 \strokec4  = containers.geometry.simplify\cf7 \strokec7 (\cf4 \strokec4 tolerance=\cf13 \cb3 \strokec13 2\cf7 \cb3 \strokec7 ,\cf4 \strokec4  preserve_topology=\cf14 \cb3 \strokec14 True\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # 3. LINKING\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 containers = containers.reset_index\cf7 \strokec7 (\cf4 \strokec4 drop=\cf14 \cb3 \strokec14 True\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 containers\cf7 \strokec7 [\cf8 \strokec8 'unique_park_id'\cf7 \strokec7 ]\cf4 \strokec4  = containers.index\cb1 \
\cb3 containers\cf7 \strokec7 [\cf8 \strokec8 'area_ha'\cf7 \strokec7 ]\cf4 \strokec4  = \cf7 \strokec7 (\cf4 \strokec4 containers\cf7 \strokec7 [\cf8 \strokec8 'area_sqm'\cf7 \strokec7 ]\cf4 \strokec4  / \cf13 \cb3 \strokec13 10000\cf7 \cb3 \strokec7 )\cf4 \strokec4 .\cf6 \strokec6 round\cf7 \strokec7 (\cf13 \cb3 \strokec13 2\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\
\cb3 amenities\cf7 \strokec7 [\cf8 \strokec8 'geometry'\cf7 \strokec7 ]\cf4 \strokec4  = amenities.geometry.apply\cf7 \strokec7 (\cf10 \cb3 \strokec10 lambda\cf4 \cb3 \strokec4  x\cf7 \strokec7 :\cf4 \strokec4  x.buffer\cf7 \strokec7 (\cf13 \cb3 \strokec13 10\cf7 \cb3 \strokec7 )\cf4 \strokec4  \cf5 \strokec5 if\cf4 \strokec4  x.geom_type == \cf8 \strokec8 'Point'\cf4 \strokec4  \cf5 \strokec5 else\cf4 \strokec4  x\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 joined_amenities = gpd.sjoin\cf7 \strokec7 (\cf4 \strokec4 amenities\cf7 \strokec7 ,\cf4 \strokec4  containers\cf7 \strokec7 ,\cf4 \strokec4  how=\cf8 \strokec8 'inner'\cf7 \strokec7 ,\cf4 \strokec4  predicate=\cf8 \strokec8 'intersects'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf9 \cb3 \strokec9 not\cf4 \cb3 \strokec4  joined_amenities.empty\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     counts = joined_amenities.groupby\cf7 \strokec7 ([\cf8 \strokec8 'unique_park_id'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'amenity_category'\cf7 \strokec7 ])\cf4 \strokec4 .size\cf7 \strokec7 ()\cf4 \strokec4 .unstack\cf7 \strokec7 (\cf4 \strokec4 fill_value=\cf13 \cb3 \strokec13 0\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3     containers_final = containers.join\cf7 \strokec7 (\cf4 \strokec4 counts\cf7 \strokec7 ,\cf4 \strokec4  on=\cf8 \strokec8 'unique_park_id'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     containers_final = containers.copy\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf4 \strokec4  col \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  \cf7 \strokec7 [\cf8 \strokec8 'Courts'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'Pitches'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'Playgrounds'\cf7 \strokec7 ]:\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 if\cf4 \strokec4  col \cf9 \cb3 \strokec9 not\cf4 \cb3 \strokec4  \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  containers_final.columns\cf7 \strokec7 :\cf4 \strokec4  containers_final\cf7 \strokec7 [\cf4 \strokec4 col\cf7 \strokec7 ]\cf4 \strokec4  = \cf13 \cb3 \strokec13 0\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 else\cf7 \strokec7 :\cf4 \strokec4  containers_final\cf7 \strokec7 [\cf4 \strokec4 col\cf7 \strokec7 ]\cf4 \strokec4  = containers_final\cf7 \strokec7 [\cf4 \strokec4 col\cf7 \strokec7 ]\cf4 \strokec4 .fillna\cf7 \strokec7 (\cf13 \cb3 \strokec13 0\cf7 \cb3 \strokec7 )\cf4 \strokec4 .astype\cf7 \strokec7 (\cf11 \cb3 \strokec11 int\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # 4. BOROUGH PROCESSING\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 boroughs_gdf = boroughs_gdf.to_crs\cf7 \strokec7 (\cf8 \strokec8 "EPSG:3857"\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'geometry'\cf7 \strokec7 ]\cf4 \strokec4  = boroughs_gdf.geometry.buffer\cf7 \strokec7 (\cf13 \cb3 \strokec13 0\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf8 \strokec8 'name'\cf4 \strokec4  \cf9 \cb3 \strokec9 not\cf4 \cb3 \strokec4  \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  boroughs_gdf.columns\cf7 \strokec7 :\cf4 \strokec4  boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'name'\cf7 \strokec7 ]\cf4 \strokec4  = \cf8 \strokec8 'Unknown'\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'name'\cf7 \strokec7 ]\cf4 \strokec4  = boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'name'\cf7 \strokec7 ]\cf4 \strokec4 .fillna\cf7 \strokec7 (\cf8 \strokec8 'Unknown'\cf7 \strokec7 )\cf4 \strokec4 .astype\cf7 \strokec7 (\cf11 \cb3 \strokec11 str\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ]\cf4 \strokec4  = boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'name'\cf7 \strokec7 ]\cf4 \strokec4 .\cf11 \cb3 \strokec11 str\cf4 \cb3 \strokec4 .replace\cf7 \strokec7 (\cf8 \strokec8 'London Borough of '\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 ''\cf7 \strokec7 )\cf4 \strokec4 .\cf11 \cb3 \strokec11 str\cf4 \cb3 \strokec4 .strip\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 def\cf4 \cb3 \strokec4  \cf6 \strokec6 clean_name\cf4 \strokec4 (\cf12 \cb3 \strokec12 n\cf4 \cb3 \strokec4 )\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 if\cf4 \strokec4  \cf9 \cb3 \strokec9 not\cf4 \cb3 \strokec4  n \cf9 \cb3 \strokec9 or\cf4 \cb3 \strokec4  n == \cf8 \strokec8 'nan'\cf7 \strokec7 :\cf4 \strokec4  \cf5 \strokec5 return\cf4 \strokec4  \cf8 \strokec8 'Unknown'\cf4 \cb1 \strokec4 \
\cb3     n = n.replace\cf7 \strokec7 (\cf8 \strokec8 'Royal Borough of '\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 ''\cf7 \strokec7 )\cf4 \strokec4 .replace\cf7 \strokec7 (\cf8 \strokec8 'London Borough of '\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 ''\cf7 \strokec7 )\cf4 \strokec4 .strip\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 if\cf4 \strokec4  n == \cf8 \strokec8 'City of Westminster'\cf7 \strokec7 :\cf4 \strokec4  \cf5 \strokec5 return\cf4 \strokec4  \cf8 \strokec8 'Westminster'\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 if\cf4 \strokec4  \cf8 \strokec8 'Greenwich'\cf4 \strokec4  \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  n\cf7 \strokec7 :\cf4 \strokec4  \cf5 \strokec5 return\cf4 \strokec4  \cf8 \strokec8 'Greenwich'\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 return\cf4 \strokec4  n\cb1 \
\
\cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'clean_name'\cf7 \strokec7 ]\cf4 \strokec4  = boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ]\cf4 \strokec4 .apply\cf7 \strokec7 (\cf4 \strokec4 clean_name\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 boroughs_gdf = boroughs_gdf\cf7 \strokec7 [\cf4 \strokec4 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'clean_name'\cf7 \strokec7 ]\cf4 \strokec4 .isin\cf7 \strokec7 (\cf4 \strokec4 OFFICIAL_BOROUGHS\cf7 \strokec7 )]\cf4 \strokec4 .copy\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ]\cf4 \strokec4  = boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'clean_name'\cf7 \strokec7 ]\cf4 \cb1 \strokec4 \
\cb3 boroughs_gdf = boroughs_gdf\cf7 \strokec7 [[\cf8 \strokec8 'borough_name'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'geometry'\cf7 \strokec7 ]]\cf4 \strokec4 .drop_duplicates\cf7 \strokec7 (\cf4 \strokec4 subset=\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ])\cf4 \cb1 \strokec4 \
\cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'boro_area_ha'\cf7 \strokec7 ]\cf4 \strokec4  = \cf7 \strokec7 (\cf4 \strokec4 boroughs_gdf.geometry.area / \cf13 \cb3 \strokec13 10000\cf7 \cb3 \strokec7 )\cf4 \strokec4 .\cf6 \strokec6 round\cf7 \strokec7 (\cf13 \cb3 \strokec13 1\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'feature_type'\cf7 \strokec7 ]\cf4 \strokec4  = \cf8 \strokec8 'borough'\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Centroids\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'centroid_lat'\cf7 \strokec7 ]\cf4 \strokec4  = boroughs_gdf.to_crs\cf7 \strokec7 (\cf4 \strokec4 epsg=\cf13 \cb3 \strokec13 4326\cf7 \cb3 \strokec7 )\cf4 \strokec4 .geometry.centroid.y\cb1 \
\cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'centroid_lon'\cf7 \strokec7 ]\cf4 \strokec4  = boroughs_gdf.to_crs\cf7 \strokec7 (\cf4 \strokec4 epsg=\cf13 \cb3 \strokec13 4326\cf7 \cb3 \strokec7 )\cf4 \strokec4 .geometry.centroid.x\cb1 \
\
\cb3 cmap = plt.get_cmap\cf7 \strokec7 (\cf8 \strokec8 'tab20'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 borough_colors = \cf7 \strokec7 \{\cf4 \strokec4 b\cf7 \strokec7 :\cf4 \strokec4  colors.to_hex\cf7 \strokec7 (\cf4 \strokec4 cmap\cf7 \strokec7 (\cf4 \strokec4 i % \cf13 \cb3 \strokec13 20\cf7 \cb3 \strokec7 ))\cf4 \strokec4  \cf5 \strokec5 for\cf4 \strokec4  i\cf7 \strokec7 ,\cf4 \strokec4  b \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  \cf6 \strokec6 enumerate\cf7 \strokec7 (\cf4 \strokec4 OFFICIAL_BOROUGHS\cf7 \strokec7 )\}\cf4 \cb1 \strokec4 \
\cb3 boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'color_hex'\cf7 \strokec7 ]\cf4 \strokec4  = boroughs_gdf\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ]\cf4 \strokec4 .\cf6 \strokec6 map\cf7 \strokec7 (\cf4 \strokec4 borough_colors\cf7 \strokec7 )\cf4 \strokec4 .fillna\cf7 \strokec7 (\cf8 \strokec8 '#cccccc'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Final Join\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 temp_parks = containers_final.copy\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\cb3 temp_parks\cf7 \strokec7 [\cf8 \strokec8 'centroid'\cf7 \strokec7 ]\cf4 \strokec4  = temp_parks.geometry.centroid\cb1 \
\cb3 temp_parks = temp_parks.set_geometry\cf7 \strokec7 (\cf8 \strokec8 'centroid'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 joined_boroughs = gpd.sjoin\cf7 \strokec7 (\cf4 \strokec4 temp_parks\cf7 \strokec7 ,\cf4 \strokec4  boroughs_gdf\cf7 \strokec7 ,\cf4 \strokec4  how=\cf8 \strokec8 'inner'\cf7 \strokec7 ,\cf4 \strokec4  predicate=\cf8 \strokec8 'intersects'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 borough_map = joined_boroughs\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ][\cf4 \strokec4 ~joined_boroughs.index.duplicated\cf7 \strokec7 (\cf4 \strokec4 keep=\cf8 \strokec8 'first'\cf7 \strokec7 )]\cf4 \cb1 \strokec4 \
\cb3 containers_final\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ]\cf4 \strokec4  = borough_map\cb1 \
\cb3 containers_final = containers_final.dropna\cf7 \strokec7 (\cf4 \strokec4 subset=\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ])\cf4 \cb1 \strokec4 \
\
\cb3 containers_final\cf7 \strokec7 [\cf8 \strokec8 'feature_type'\cf7 \strokec7 ]\cf4 \strokec4  = \cf8 \strokec8 'park'\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Solid Polygons\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 containers_final\cf7 \strokec7 [\cf8 \strokec8 'geometry'\cf7 \strokec7 ]\cf4 \strokec4  = containers_final.geometry.apply\cf7 \strokec7 (\cf4 \cb1 \strokec4 \
\cb3     \cf10 \cb3 \strokec10 lambda\cf4 \cb3 \strokec4  geom\cf7 \strokec7 :\cf4 \strokec4  geom.buffer\cf7 \strokec7 (\cf13 \cb3 \strokec13 10\cf7 \cb3 \strokec7 )\cf4 \strokec4  \cf5 \strokec5 if\cf4 \strokec4  geom.geom_type == \cf8 \strokec8 'Point'\cf4 \strokec4  \cf5 \strokec5 else\cf4 \strokec4  geom\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # 5. STATS\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 stats_df = containers_final.groupby\cf7 \strokec7 (\cf8 \strokec8 'borough_name'\cf7 \strokec7 )\cf4 \strokec4 .agg\cf7 \strokec7 (\{\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 'name'\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 'count'\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 'Courts'\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 'sum'\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 'Playgrounds'\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 'sum'\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 'area_ha'\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 'sum'\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 \})\cf4 \strokec4 .rename\cf7 \strokec7 (\cf4 \strokec4 columns=\cf7 \strokec7 \{\cf8 \strokec8 'name'\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 'total_parks'\cf7 \strokec7 \})\cf4 \strokec4 .reset_index\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 stats_df = stats_df.merge\cf7 \strokec7 (\cf4 \strokec4 boroughs_gdf\cf7 \strokec7 [[\cf8 \strokec8 'borough_name'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'boro_area_ha'\cf7 \strokec7 ]],\cf4 \strokec4  on=\cf8 \strokec8 'borough_name'\cf7 \strokec7 ,\cf4 \strokec4  how=\cf8 \strokec8 'left'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 stats_df\cf7 \strokec7 [\cf8 \strokec8 'ratio_pct'\cf7 \strokec7 ]\cf4 \strokec4  = \cf7 \strokec7 ((\cf4 \strokec4 stats_df\cf7 \strokec7 [\cf8 \strokec8 'area_ha'\cf7 \strokec7 ]\cf4 \strokec4  / stats_df\cf7 \strokec7 [\cf8 \strokec8 'boro_area_ha'\cf7 \strokec7 ])\cf4 \strokec4  * \cf13 \cb3 \strokec13 100\cf7 \cb3 \strokec7 )\cf4 \strokec4 .\cf6 \strokec6 round\cf7 \strokec7 (\cf13 \cb3 \strokec13 1\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 borough_stats_json = stats_df.set_index\cf7 \strokec7 (\cf8 \strokec8 'borough_name'\cf7 \strokec7 )\cf4 \strokec4 .to_json\cf7 \strokec7 (\cf4 \strokec4 orient=\cf8 \strokec8 'index'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # 6. MAP CONSTRUCTION\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf7 \strokec7 (\cf8 \strokec8 "\uc0\u55357 \u56826 \u65039   Building Map..."\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 gdf_map = containers_final.to_crs\cf7 \strokec7 (\cf4 \strokec4 epsg=\cf13 \cb3 \strokec13 4326\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 boroughs_map = boroughs_gdf.to_crs\cf7 \strokec7 (\cf4 \strokec4 epsg=\cf13 \cb3 \strokec13 4326\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 min_lon\cf7 \strokec7 ,\cf4 \strokec4  min_lat\cf7 \strokec7 ,\cf4 \strokec4  max_lon\cf7 \strokec7 ,\cf4 \strokec4  max_lat = boroughs_map.total_bounds\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 def\cf4 \cb3 \strokec4  \cf6 \strokec6 create_popup\cf4 \strokec4 (\cf12 \cb3 \strokec12 row\cf4 \cb3 \strokec4 )\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     name = \cf11 \cb3 \strokec11 str\cf7 \cb3 \strokec7 (\cf4 \strokec4 row\cf7 \strokec7 [\cf8 \strokec8 'name'\cf7 \strokec7 ])\cf4 \cb1 \strokec4 \
\cb3     safe_name = name.replace\cf7 \strokec7 (\cf8 \strokec8 "'"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "\\\\'"\cf7 \strokec7 )\cf4 \strokec4  \cf5 \strokec5 if\cf4 \strokec4  name \cf9 \cb3 \strokec9 and\cf4 \cb3 \strokec4  name != \cf8 \strokec8 'nan'\cf4 \strokec4  \cf5 \strokec5 else\cf4 \strokec4  \cf8 \strokec8 "Open Space"\cf4 \cb1 \strokec4 \
\cb3     safe_borough = \cf11 \cb3 \strokec11 str\cf7 \cb3 \strokec7 (\cf4 \strokec4 row\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ])\cf4 \strokec4 .replace\cf7 \strokec7 (\cf8 \strokec8 "'"\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 "\\\\'"\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3     unique_id = hashlib.md5\cf7 \strokec7 ((\cf4 \strokec4 safe_name + safe_borough\cf7 \strokec7 )\cf4 \strokec4 .encode\cf7 \strokec7 ())\cf4 \strokec4 .hexdigest\cf7 \strokec7 ()\cf4 \cb1 \strokec4 \
\
\cb3     p_type = \cf8 \strokec8 "Green Space"\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 if\cf4 \strokec4  \cf8 \strokec8 'wood'\cf4 \strokec4  \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  \cf11 \cb3 \strokec11 str\cf7 \cb3 \strokec7 (\cf4 \strokec4 row.get\cf7 \strokec7 (\cf8 \strokec8 'natural'\cf7 \strokec7 ,\cf8 \strokec8 ''\cf7 \strokec7 )):\cf4 \strokec4  p_type = \cf8 \strokec8 "Woodland"\cf4 \cb1 \strokec4 \
\
\cb3     c_badge = \cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 '<span class="badge" style="background:#e65100; color:white;">\uc0\u55356 \u57278  \cf7 \strokec7 \{\cf4 \strokec4 row.get\cf7 \strokec7 (\cf8 \strokec8 "Courts"\cf7 \strokec7 ,\cf13 \cb3 \strokec13 0\cf7 \cb3 \strokec7 )\}\cf8 \strokec8 </span>'\cf4 \strokec4  \cf5 \strokec5 if\cf4 \strokec4  row.get\cf7 \strokec7 (\cf8 \strokec8 'Courts'\cf7 \strokec7 ,\cf4 \strokec4  \cf13 \cb3 \strokec13 0\cf7 \cb3 \strokec7 )\cf4 \strokec4  > \cf13 \cb3 \strokec13 0\cf4 \cb3 \strokec4  \cf5 \strokec5 else\cf4 \strokec4  \cf8 \strokec8 ""\cf4 \cb1 \strokec4 \
\cb3     p_badge = \cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 '<span class="badge" style="background:#9b59b6; color:white;">\uc0\u55358 \u56824  \cf7 \strokec7 \{\cf4 \strokec4 row.get\cf7 \strokec7 (\cf8 \strokec8 "Playgrounds"\cf7 \strokec7 ,\cf13 \cb3 \strokec13 0\cf7 \cb3 \strokec7 )\}\cf8 \strokec8 </span>'\cf4 \strokec4  \cf5 \strokec5 if\cf4 \strokec4  row.get\cf7 \strokec7 (\cf8 \strokec8 'Playgrounds'\cf7 \strokec7 ,\cf4 \strokec4  \cf13 \cb3 \strokec13 0\cf7 \cb3 \strokec7 )\cf4 \strokec4  > \cf13 \cb3 \strokec13 0\cf4 \cb3 \strokec4  \cf5 \strokec5 else\cf4 \strokec4  \cf8 \strokec8 ""\cf4 \cb1 \strokec4 \
\
\cb3     \cf5 \strokec5 return\cf4 \strokec4  \cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8     <div style=\cf4 \strokec4 "\cf8 \strokec8 font-family:'Segoe UI'; width:200px;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <h4 style=\cf4 \strokec4 "\cf8 \strokec8 margin:0 0 2px 0;\cf4 \strokec4 "\cf8 \strokec8 >\cf7 \strokec7 \{\cf4 \strokec4 safe_name\cf7 \strokec7 \}\cf8 \strokec8 </h4>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <div style=\cf4 \strokec4 "\cf8 \strokec8 font-size:10px; color:#666;\cf4 \strokec4 "\cf8 \strokec8 >\cf7 \strokec7 \{\cf4 \strokec4 p_type\cf7 \strokec7 \}\cf8 \strokec8  \'95 \cf7 \strokec7 \{\cf4 \strokec4 safe_borough\cf7 \strokec7 \}\cf8 \strokec8 </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <div style=\cf4 \strokec4 "\cf8 \strokec8 font-size:11px; margin-bottom:8px;\cf4 \strokec4 "\cf8 \strokec8 >\uc0\u55357 \u56527  \cf7 \strokec7 \{\cf4 \strokec4 row\cf7 \strokec7 [\cf8 \strokec8 'area_ha'\cf7 \strokec7 ]\}\cf8 \strokec8  ha</div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <div style=\cf4 \strokec4 "\cf8 \strokec8 margin-bottom:12px;\cf4 \strokec4 "\cf8 \strokec8 >\cf7 \strokec7 \{\cf4 \strokec4 c_badge\cf7 \strokec7 \}\cf8 \strokec8  \cf7 \strokec7 \{\cf4 \strokec4 p_badge\cf7 \strokec7 \}\cf8 \strokec8 </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <div style=\cf4 \strokec4 "\cf8 \strokec8 display:flex; gap:5px;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             <button id=\cf4 \strokec4 "\cf8 \strokec8 btn-\cf7 \strokec7 \{\cf4 \strokec4 unique_id\cf7 \strokec7 \}\cf4 \strokec4 "\cf8 \strokec8  onclick=\cf4 \strokec4 "\cf8 \strokec8 sendToSheet('\cf7 \strokec7 \{\cf4 \strokec4 safe_name\cf7 \strokec7 \}\cf8 \strokec8 ', '\cf7 \strokec7 \{\cf4 \strokec4 safe_borough\cf7 \strokec7 \}\cf8 \strokec8 ', '\cf7 \strokec7 \{\cf4 \strokec4 p_type\cf7 \strokec7 \}\cf8 \strokec8 ', '\cf7 \strokec7 \{\cf4 \strokec4 row.get\cf7 \strokec7 (\cf8 \strokec8 'Courts'\cf7 \strokec7 ,\cf13 \cb3 \strokec13 0\cf7 \cb3 \strokec7 )\}\cf8 \strokec8 ', '\cf7 \strokec7 \{\cf4 \strokec4 unique_id\cf7 \strokec7 \}\cf8 \strokec8 ', this)\cf4 \strokec4 "\cb1 \
\cf8 \cb3 \strokec8                 style=\cf4 \strokec4 "\cf8 \strokec8 flex:1; background:#27ae60; color:white; padding:6px; border:none; border-radius:4px; cursor:pointer; font-weight:bold;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 + Add Pod\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             </button>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     """\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 gdf_map\cf7 \strokec7 [\cf8 \strokec8 'popup_html'\cf7 \strokec7 ]\cf4 \strokec4  = gdf_map.apply\cf7 \strokec7 (\cf4 \strokec4 create_popup\cf7 \strokec7 ,\cf4 \strokec4  axis=\cf13 \cb3 \strokec13 1\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\
\cb3 m = folium.Map\cf7 \strokec7 (\cf4 \strokec4 tiles=\cf8 \strokec8 'CartoDB positron'\cf7 \strokec7 ,\cf4 \strokec4  zoom_start=\cf13 \cb3 \strokec13 10\cf7 \cb3 \strokec7 ,\cf4 \strokec4  prefer_canvas=\cf14 \cb3 \strokec14 True\cf7 \cb3 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 m.fit_bounds\cf7 \strokec7 ([[\cf4 \strokec4 min_lat\cf7 \strokec7 ,\cf4 \strokec4  min_lon\cf7 \strokec7 ],\cf4 \strokec4  \cf7 \strokec7 [\cf4 \strokec4 max_lat\cf7 \strokec7 ,\cf4 \strokec4  max_lon\cf7 \strokec7 ]])\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Tile Layers\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 folium.TileLayer\cf7 \strokec7 (\cf8 \strokec8 'openstreetmap'\cf7 \strokec7 ,\cf4 \strokec4  name=\cf8 \strokec8 'Standard'\cf7 \strokec7 )\cf4 \strokec4 .add_to\cf7 \strokec7 (\cf4 \strokec4 m\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 folium.TileLayer\cf7 \strokec7 (\cf8 \strokec8 'cartodbdark_matter'\cf7 \strokec7 ,\cf4 \strokec4  name=\cf8 \strokec8 'Dark'\cf7 \strokec7 )\cf4 \strokec4 .add_to\cf7 \strokec7 (\cf4 \strokec4 m\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3 Fullscreen\cf7 \strokec7 ()\cf4 \strokec4 .add_to\cf7 \strokec7 (\cf4 \strokec4 m\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # 1. BOROUGHS & LABELS\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 folium.GeoJson\cf7 \strokec7 (\cf4 \cb1 \strokec4 \
\cb3     boroughs_map\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     name=\cf8 \strokec8 "\uc0\u55356 \u56812 \u55356 \u56807  Boroughs"\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     style_function=\cf10 \cb3 \strokec10 lambda\cf4 \cb3 \strokec4  x\cf7 \strokec7 :\cf4 \strokec4  \cf7 \strokec7 \{\cf4 \cb1 \strokec4 \
\cb3         \cf8 \strokec8 'fillColor'\cf7 \strokec7 :\cf4 \strokec4  x\cf7 \strokec7 [\cf8 \strokec8 'properties'\cf7 \strokec7 ]\cf4 \strokec4 .get\cf7 \strokec7 (\cf8 \strokec8 'color_hex'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 '#555'\cf7 \strokec7 ),\cf4 \cb1 \strokec4 \
\cb3         \cf8 \strokec8 'color'\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 '#555555'\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3         \cf8 \strokec8 'weight'\cf7 \strokec7 :\cf4 \strokec4  \cf13 \cb3 \strokec13 1\cf7 \cb3 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3         \cf8 \strokec8 'fillOpacity'\cf7 \strokec7 :\cf4 \strokec4  \cf13 \cb3 \strokec13 0.15\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 \},\cf4 \cb1 \strokec4 \
\cb3     tooltip=folium.GeoJsonTooltip\cf7 \strokec7 (\cf4 \strokec4 fields=\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ])\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 )\cf4 \strokec4 .add_to\cf7 \strokec7 (\cf4 \strokec4 m\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf4 \strokec4  _\cf7 \strokec7 ,\cf4 \strokec4  row \cf9 \cb3 \strokec9 in\cf4 \cb3 \strokec4  boroughs_map.iterrows\cf7 \strokec7 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 if\cf4 \strokec4  \cf9 \cb3 \strokec9 not\cf4 \cb3 \strokec4  pd.isna\cf7 \strokec7 (\cf4 \strokec4 row\cf7 \strokec7 [\cf8 \strokec8 'centroid_lat'\cf7 \strokec7 ]):\cf4 \cb1 \strokec4 \
\cb3         folium.Marker\cf7 \strokec7 (\cf4 \cb1 \strokec4 \
\cb3             location=\cf7 \strokec7 [\cf4 \strokec4 row\cf7 \strokec7 [\cf8 \strokec8 'centroid_lat'\cf7 \strokec7 ],\cf4 \strokec4  row\cf7 \strokec7 [\cf8 \strokec8 'centroid_lon'\cf7 \strokec7 ]],\cf4 \cb1 \strokec4 \
\cb3             icon=folium.DivIcon\cf7 \strokec7 (\cf4 \strokec4 html=\cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8                 <div class=\cf4 \strokec4 "\cf8 \strokec8 borough-label\cf4 \strokec4 "\cf8 \strokec8  data-borough=\cf4 \strokec4 "\cf7 \strokec7 \{\cf4 \strokec4 row\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ]\}\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cb1 \
\cf8 \cb3 \strokec8                     font-family:'Segoe UI'; font-size:10px; font-weight:bold; color:#444;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     text-shadow: 1px 1px 0 rgba(255,255,255,0.8); text-align:center;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     width:120px; margin-left:-60px; pointer-events:none;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     \cf7 \strokec7 \{\cf4 \strokec4 row\cf7 \strokec7 [\cf8 \strokec8 'borough_name'\cf7 \strokec7 ]\cf4 \strokec4 .upper\cf7 \strokec7 ()\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             """\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3         \cf7 \strokec7 )\cf4 \strokec4 .add_to\cf7 \strokec7 (\cf4 \strokec4 m\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # 2. PARKS\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 def\cf4 \cb3 \strokec4  \cf6 \strokec6 park_style\cf4 \strokec4 (\cf12 \cb3 \strokec12 feature\cf4 \cb3 \strokec4 )\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 return\cf4 \strokec4  \cf7 \strokec7 \{\cf8 \strokec8 'fillColor'\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 '#00e676'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'color'\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 '#1b5e20'\cf7 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'weight'\cf7 \strokec7 :\cf4 \strokec4  \cf13 \cb3 \strokec13 1\cf7 \cb3 \strokec7 ,\cf4 \strokec4  \cf8 \strokec8 'fillOpacity'\cf7 \strokec7 :\cf4 \strokec4  \cf13 \cb3 \strokec13 1\cf7 \cb3 \strokec7 \}\cf4 \cb1 \strokec4 \
\
\cb3 folium.GeoJson\cf7 \strokec7 (\cf4 \cb1 \strokec4 \
\cb3     gdf_map\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     name=\cf8 \strokec8 "\uc0\u55356 \u57139  Pod Locations"\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     style_function=park_style\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cb3     popup=folium.GeoJsonPopup\cf7 \strokec7 (\cf4 \strokec4 fields=\cf7 \strokec7 [\cf8 \strokec8 'popup_html'\cf7 \strokec7 ],\cf4 \strokec4  labels=\cf14 \cb3 \strokec14 False\cf7 \cb3 \strokec7 ),\cf4 \cb1 \strokec4 \
\cb3     tooltip=folium.GeoJsonTooltip\cf7 \strokec7 (\cf4 \strokec4 fields=\cf7 \strokec7 [\cf8 \strokec8 'name'\cf7 \strokec7 ]),\cf4 \cb1 \strokec4 \
\cb3     embed=\cf14 \cb3 \strokec14 True\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 )\cf4 \strokec4 .add_to\cf7 \strokec7 (\cf4 \strokec4 m\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 folium.LayerControl\cf7 \strokec7 (\cf4 \strokec4 collapsed=\cf14 \cb3 \strokec14 True\cf7 \cb3 \strokec7 )\cf4 \strokec4 .add_to\cf7 \strokec7 (\cf4 \strokec4 m\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- DASHBOARD UI ---\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 dashboard_html = \cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 <div id=\cf4 \strokec4 "\cf8 \strokec8 ui-panel\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cb1 \
\cf8 \cb3 \strokec8     position: fixed; top: 140px; right: 20px; z-index: 9000;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     width: 320px;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     background: #2c3e50;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     border-radius: 4px;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     font-family: 'Segoe UI', sans-serif;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     overflow: hidden;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     color: white;\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8     <div style=\cf4 \strokec4 "\cf8 \strokec8 padding: 15px; border-bottom: 1px solid #34495e;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <div style=\cf4 \strokec4 "\cf8 \strokec8 font-size: 11px; font-weight: 700; text-transform: uppercase; color: #bdc3c7;\cf4 \strokec4 "\cf8 \strokec8 >LOCATION IDENTIFIER</div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <div style=\cf4 \strokec4 "\cf8 \strokec8 display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-top: 15px;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             <div style=\cf4 \strokec4 "\cf8 \strokec8 text-align:center;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 <div id=\cf4 \strokec4 "\cf8 \strokec8 sum-parks\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 font-size: 20px; font-weight: 700;\cf4 \strokec4 "\cf8 \strokec8 >0</div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 <div style=\cf4 \strokec4 "\cf8 \strokec8 font-size:10px; color:#bdc3c7;\cf4 \strokec4 "\cf8 \strokec8 >Locations</div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             <div style=\cf4 \strokec4 "\cf8 \strokec8 text-align:center;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 <div id=\cf4 \strokec4 "\cf8 \strokec8 sum-courts\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 font-size: 20px; font-weight: 700;\cf4 \strokec4 "\cf8 \strokec8 >0</div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 <div style=\cf4 \strokec4 "\cf8 \strokec8 font-size:10px; color:#bdc3c7;\cf4 \strokec4 "\cf8 \strokec8 >Courts</div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             <div style=\cf4 \strokec4 "\cf8 \strokec8 text-align:center;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 <div id=\cf4 \strokec4 "\cf8 \strokec8 sum-play\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 font-size: 20px; font-weight: 700;\cf4 \strokec4 "\cf8 \strokec8 >0</div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 <div style=\cf4 \strokec4 "\cf8 \strokec8 font-size:10px; color:#bdc3c7;\cf4 \strokec4 "\cf8 \strokec8 >Playgrounds</div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     </div>\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8     <div style=\cf4 \strokec4 "\cf8 \strokec8 background: #ecf0f1; padding: 10px; display:flex; flex-direction:column; gap:5px; color:#2c3e50; border-bottom:1px solid #ddd;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <label style=\cf4 \strokec4 "\cf8 \strokec8 font-size:11px; font-weight:600; cursor:pointer; display:flex; align-items:center;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             <input type=\cf4 \strokec4 "\cf8 \strokec8 checkbox\cf4 \strokec4 "\cf8 \strokec8  id=\cf4 \strokec4 "\cf8 \strokec8 chk-highval\cf4 \strokec4 "\cf8 \strokec8  onchange=\cf4 \strokec4 "\cf8 \strokec8 updateMapState()\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 margin-right:5px;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             Only Show Sports/Play\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         </label>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <label style=\cf4 \strokec4 "\cf8 \strokec8 font-size:11px; font-weight:600; cursor:pointer; display:flex; align-items:center;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             <input type=\cf4 \strokec4 "\cf8 \strokec8 checkbox\cf4 \strokec4 "\cf8 \strokec8  id=\cf4 \strokec4 "\cf8 \strokec8 chk-bookedonly\cf4 \strokec4 "\cf8 \strokec8  onchange=\cf4 \strokec4 "\cf8 \strokec8 updateMapState()\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 margin-right:5px;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             Show Booked Only \uc0\u55357 \u56594 \cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         </label>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <div id=\cf4 \strokec4 "\cf8 \strokec8 sheet-status\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 font-size:10px; font-weight:bold; color:#27ae60; margin-top:2px;\cf4 \strokec4 "\cf8 \strokec8 >\uc0\u9679  Live</div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     </div>\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8     <div style=\cf4 \strokec4 "\cf8 \strokec8 background: white; height: 450px; display: flex; flex-direction: column;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         <div style=\cf4 \strokec4 "\cf8 \strokec8 padding: 8px 12px; background: #f8f9fa; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; color: #7f8c8d;\cf4 \strokec4 "\cf8 \strokec8 >\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             <span style=\cf4 \strokec4 "\cf8 \strokec8 font-size: 10px; font-weight: 700;\cf4 \strokec4 "\cf8 \strokec8 >BOROUGH VISIBILITY</span>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             <div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 <button onclick=\cf4 \strokec4 "\cf8 \strokec8 toggleAll(true)\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 font-size: 9px; padding: 2px 6px; border: 1px solid #ccc; background: white; cursor:pointer;\cf4 \strokec4 "\cf8 \strokec8 >All</button>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 <button onclick=\cf4 \strokec4 "\cf8 \strokec8 toggleAll(false)\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 font-size: 9px; padding: 2px 6px; border: 1px solid #ccc; background: white; cursor:pointer;\cf4 \strokec4 "\cf8 \strokec8 >None</button>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         </div>\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8         <div id=\cf4 \strokec4 "\cf8 \strokec8 borough-list\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 overflow-y: auto; flex-grow: 1; color: #333;\cf4 \strokec4 "\cf8 \strokec8 ></div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     </div>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8 </div>\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8 <script>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     var boroughStats = \cf7 \strokec7 \{\cf4 \strokec4 borough_stats_json\cf7 \strokec7 \}\cf8 \strokec8 ;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     var allBoroughs = Object.keys(boroughStats).sort();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     var activeBoroughs = new Set(allBoroughs);\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     var existingParks = new Set();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     var SCRIPT_URL = \cf4 \strokec4 "\cf7 \strokec7 \{\cf4 \strokec4 GOOGLE_SCRIPT_URL\cf7 \strokec7 \}\cf4 \strokec4 "\cf8 \strokec8 ;\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8     // --- HELPER FOR MATCHING (CRITICAL FIX) ---\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     function normalize(str) \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         return str ? str.toLowerCase().replace(/[^a-z0-9]/g, '') : '';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     \}\}\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8     function startConnectionEngine() \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         var statusEl = document.getElementById('sheet-status');\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         function tryConnect() \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             fetch(SCRIPT_URL + \cf4 \strokec4 "\cf8 \strokec8 ?action=read\cf4 \strokec4 "\cf8 \strokec8 )\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             .then(r => r.json())\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             .then(data => \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 if(data.names)\{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     data.names.forEach(n => existingParks.add(normalize(n)));\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     updateMapState();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     statusEl.innerText = \cf4 \strokec4 "\cf8 \strokec8 \uc0\u9679  Live\cf4 \strokec4 "\cf8 \strokec8 ; statusEl.style.color = \cf4 \strokec4 "\cf8 \strokec8 #27ae60\cf4 \strokec4 "\cf8 \strokec8 ;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 \}\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             \}\})\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             .catch(e => \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 statusEl.innerText = \cf4 \strokec4 "\cf8 \strokec8 \uc0\u8635  Syncing\cf4 \strokec4 "\cf8 \strokec8 ; statusEl.style.color = \cf4 \strokec4 "\cf8 \strokec8 #e67e22\cf4 \strokec4 "\cf8 \strokec8 ;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 setTimeout(tryConnect, 5000);\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             \}\});\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         \}\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         tryConnect();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     \}\}\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8     // --- MAIN MAP UPDATE LOGIC ---\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     function updateMapState() \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         var tP=0, tC=0, tPl=0;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         var showHighValue = document.getElementById('chk-highval').checked;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         var showBookedOnly = document.getElementById('chk-bookedonly').checked;\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8         var map = null; for(var k in window)\{\{ if(window[k] instanceof L.Map)\{\{ map=window[k]; break; \}\} \}\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         if(!map) return;\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8         map.eachLayer(l => \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             var props = l.feature ? l.feature.properties : null;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             if(!props) return;\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8             // --- BOROUGH LOGIC (Independent) ---\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             if (props.feature_type === 'borough') \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 var showBorough = activeBoroughs.has(props.borough_name);\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8                 // BOROUGHS are NOT filtered by \cf4 \strokec4 "\cf8 \strokec8 Booked Only\cf4 \strokec4 "\cf8 \strokec8  - they stay for context\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 // Only hide if the checkbox is unchecked\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 if (showBorough) \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     var c = props.color_hex || '#555';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     // RESTORE COLOR\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     l.setStyle(\{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         opacity: 1,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         fillOpacity: 0.15,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         stroke: true,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         fill: true,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         color: '#555',\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         fillColor: c,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         weight: 1.5\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     \}\});\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 \}\} else \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     l.setStyle(\{\{ opacity: 0, fillOpacity: 0, stroke: false, fill: false \}\});\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 \}\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             \}\}\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8             // --- PARK LOGIC (Filters applied here) ---\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             else if (props.feature_type === 'park') \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 var showPark = activeBoroughs.has(props.borough_name);\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8                 // Only apply filters if parent borough is active\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 if (showPark) \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     var hasAmenities = (props.Courts > 0 || props.Playgrounds > 0);\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     var isBooked = existingParks.has(normalize(props.name));\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8                     if (showHighValue && !hasAmenities) showPark = false;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     if (showBookedOnly && !isBooked) showPark = false;\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8                     if (showPark) \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         // Count visible stats\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         tP++; tC += (props.Courts || 0); tPl += (props.Playgrounds || 0);\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8                         // STYLE LOGIC\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         if (isBooked) \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                             // LOCKED STYLE\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                             l.setStyle(\{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 opacity: 1,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 fillOpacity: 1.0,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 stroke: true,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 fill: true,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 color: '#333',\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 fillColor: '#2c3e50', // GREY\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 weight: 1\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                             \}\});\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                             l.interactive = false;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         \}\} else \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                             // AVAILABLE STYLE\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                             var isSports = (props.Courts > 0);\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                             l.setStyle(\{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 opacity: 1,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 fillOpacity: 1.0,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 weight: 1,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 stroke: true,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 fill: true,\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 color: '#333',\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                                 fillColor: isSports ? '#ff6d00' : '#00e676' // ORANGE / GREEN\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                             \}\});\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                             l.interactive = true;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                         \}\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     \}\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 \}\}\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8                 if (!showPark) \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     l.setStyle(\{\{ opacity: 0, fillOpacity: 0, stroke: false, fill: false \}\});\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     if (l.unbindTooltip) l.unbindTooltip();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                     l.interactive = false;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8                 \}\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             \}\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         \}\});\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8         // Update Labels\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         var labels = document.getElementsByClassName('borough-label');\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         for(var i=0; i<labels.length; i++) \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             var bName = labels[i].getAttribute('data-borough');\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             labels[i].style.display = activeBoroughs.has(bName) ? 'block' : 'none';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         \}\}\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8         document.getElementById('sum-parks').innerText = tP.toLocaleString();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         document.getElementById('sum-courts').innerText = tC.toLocaleString();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         document.getElementById('sum-play').innerText = tPl.toLocaleString();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     \}\}\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8     var listContainer = document.getElementById('borough-list');\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     function renderList() \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         var html = '';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         allBoroughs.forEach(b => \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             var isChecked = activeBoroughs.has(b) ? 'checked' : '';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             var s = boroughStats[b];\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8             html += '<div style=\cf4 \strokec4 "\cf8 \strokec8 padding:10px; border-bottom:1px solid #f1f3f5; display:flex; align-items:center; font-size:12px;\cf4 \strokec4 "\cf8 \strokec8 >';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             html += '<input type=\cf4 \strokec4 "\cf8 \strokec8 checkbox\cf4 \strokec4 "\cf8 \strokec8  ' + isChecked + ' onchange=\cf4 \strokec4 "\cf8 \strokec8 updateState(\\\\''+b+'\\\\', this.checked)\cf4 \strokec4 "\cf8 \strokec8  style=\cf4 \strokec4 "\cf8 \strokec8 margin-right:10px; cursor:pointer;\cf4 \strokec4 "\cf8 \strokec8 >';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             html += '<span style=\cf4 \strokec4 "\cf8 \strokec8 flex:1; font-weight:500;\cf4 \strokec4 "\cf8 \strokec8 >' + b + '</span>';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             html += '<span style=\cf4 \strokec4 "\cf8 \strokec8 background:#eee; padding:2px 6px; border-radius:4px; font-size:10px; margin-left:5px;\cf4 \strokec4 "\cf8 \strokec8 >' + s.Courts + ' \uc0\u9917 </span>';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             html += '</div>';\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         \}\});\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         listContainer.innerHTML = html;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         updateMapState();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     \}\}\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8     window.updateState = function(b, c) \{\{ if(c) activeBoroughs.add(b); else activeBoroughs.delete(b); updateMapState(); \}\};\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     window.toggleAll = function(s) \{\{ if(s) activeBoroughs = new Set(allBoroughs); else activeBoroughs = new Set(); renderList(); \}\};\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8     window.sendToSheet = function(n, b, t, c, u, btn) \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         if(existingParks.has(normalize(n))) \{\{ alert(\cf4 \strokec4 "\cf8 \strokec8 \uc0\u9888 \u65039  Already added!\cf4 \strokec4 "\cf8 \strokec8 ); return; \}\}\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         btn.innerText = \cf4 \strokec4 "\cf8 \strokec8 Saving...\cf4 \strokec4 "\cf8 \strokec8 ;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         fetch(SCRIPT_URL + \cf4 \strokec4 "\cf8 \strokec8 ?action=add&name=\cf4 \strokec4 "\cf8 \strokec8 +encodeURIComponent(n)+\cf4 \strokec4 "\cf8 \strokec8 &borough=\cf4 \strokec4 "\cf8 \strokec8 +encodeURIComponent(b)+\cf4 \strokec4 "\cf8 \strokec8 &type=\cf4 \strokec4 "\cf8 \strokec8 +encodeURIComponent(t)+\cf4 \strokec4 "\cf8 \strokec8 &courts=\cf4 \strokec4 "\cf8 \strokec8 +c)\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         .then(r => \{\{\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             btn.innerText = \cf4 \strokec4 "\cf8 \strokec8 LOCKED\cf4 \strokec4 "\cf8 \strokec8 ; btn.style.background = \cf4 \strokec4 "\cf8 \strokec8 #2c3e50\cf4 \strokec4 "\cf8 \strokec8 ; btn.disabled=true;\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             existingParks.add(normalize(n));\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8             updateMapState();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8         \}\});\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     \}\};\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8     startConnectionEngine();\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     setTimeout(renderList, 1500);\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8 </script>\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 m.get_root\cf7 \strokec7 ()\cf4 \strokec4 .html.add_child\cf7 \strokec7 (\cf4 \strokec4 folium.Element\cf7 \strokec7 (\cf4 \strokec4 dashboard_html\cf7 \strokec7 ))\cf4 \cb1 \strokec4 \
\
\cb3 output_file = \cf8 \strokec8 "London_Location_Identifier_v41_LogicOverhaul.html"\cf4 \cb1 \strokec4 \
\cb3 m.save\cf7 \strokec7 (\cf4 \strokec4 output_file\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf7 \strokec7 (\cf10 \cb3 \strokec10 f\cf8 \cb3 \strokec8 "\uc0\u9989  Logic Overhaul Dashboard generated: \cf7 \strokec7 \{\cf4 \strokec4 output_file\cf7 \strokec7 \}\cf8 \strokec8 "\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cf6 \cb3 \strokec6 print\cf7 \strokec7 (\cf8 \strokec8 "\uc0\u11015 \u65039   Downloading file now..."\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 files.download\cf7 \strokec7 (\cf4 \strokec4 output_file\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
}