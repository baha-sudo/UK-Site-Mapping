# Loom Link https://www.loom.com/share/7a581b854d7d43019867e37716930532
# 🇬🇧 UK Site Intelligence & Operations Dashboard

This repository contains a suite of tools designed to map UK parks, identify valid installation sites for pods, and manage operations via a synchronized dashboard. It integrates **Google Sheets**, **Notion**, and **Interactive Maps** (Leaflet/Folium).

## 📂 Repository Structure

* **`backend/`**: Contains the Google Apps Script code (`Code.gs`) that powers the Google Sheet webhook, handles locking to prevent duplicate entries, and syncs data to Notion.
* **`python_scripts/`**: Python pipelines (designed for Google Colab) to process geospatial data and generate the dashboards.
* **`maps/`**: The final output HTML files containing the interactive maps.

---

## 💾 Required Data (Large Files)

The geospatial data files (`.gpkg`) required to run the Location Identifier are too large to be hosted directly on GitHub.

👉 **[Click here to download the Data Files from Google Drive](https://drive.google.com/drive/folders/1JQpS_-FdWEm1yzE-8WVbusZj--iN4r4_?usp=sharing)**

### Data Setup Instructions:
1.  Download the two files: `london_parks_master.gpkg` and `london_boroughs_master.gpkg`.
2.  Create a folder on your Google Drive named **`LondonMapData`**.
3.  Upload the two `.gpkg` files into that folder.
    * *Note: The Python scripts are configured to look for this specific folder path in Google Drive.*

---

## ⚙️ Configuration & Setup

### 1. Backend (Google Sheets)
1.  Open your Master Google Sheet.
2.  Go to **Extensions > Apps Script**.
3.  Copy the code from `backend/Code.gs` and paste it into the script editor.
4.  **Important:** Replace `const NOTION_TOKEN = "..."` with your actual Notion API Integration Token.
5.  Deploy the script as a Web App to generate the Webhook URL.

### 2. Python Pipelines (Google Colab)
The scripts in `python_scripts/` are designed to run in a Google Colab environment.

* **`uk_dashboard_generator.py`**: Generates the "UK Installation Map" with route optimization and approval filters.
* **`location_identifier.py`**: Runs the "Logic Overhaul" analysis to find new sites based on specific criteria (Size > 2000sqm, Amenities, etc.).

**To run them:**
1.  Upload the `.py` file to Google Colab.
2.  Ensure you have mounted your Google Drive (the script handles this).
3.  **Security Note:** Update the `NOTION_TOKEN` and `DATABASE_ID` variables in the script before running.

---

## 🚀 Features

* **Real-time Locking:** Prevents two users from "booking" the same site simultaneously via the Google Sheet Webhook.
* **Notion Sync:** Automatically pushes valid sites to a Notion Database and cleans up duplicates.
* **Route Optimization:** The UK Dashboard includes a "Plan Cycle Route" feature that optimizes the travel path between selected sites using a greedy nearest-neighbor algorithm.
* **Smart Filtering:** The Location Identifier filters out cemeteries, religious grounds, and small sites automatically.

---

## ⚠️ Security Warning

This code requires API Tokens to function.
* **Never commit your actual API keys to GitHub.**
* Always use environment variables or local placeholders when sharing code.
