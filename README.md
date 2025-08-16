
# Vahan Investor Dashboard (Sample)

A Streamlit dashboard for analyzing vehicle registrations by category (2W/3W/4W) and manufacturer, with YoY and QoQ growth—designed for investor-style analysis.

> **Note**: The repository ships with **synthetic sample data**. Replace `data/registrations_sample.csv` with an export from the official Vahan dashboard to analyze real trends.

## Features
- Category & manufacturer filters
- Date range selection
- Trend charts for registrations
- **YoY%** and **QoQ%** growth for categories and each manufacturer
- Clean, investor-friendly UI in Streamlit

## Quickstart
```bash
# 1) Create & activate a virtualenv (optional but recommended)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run
streamlit run app.py
```

### Data
- Default file: `data/registrations_sample.csv` (synthetic).
- To use real data, export/scrape into a CSV with columns:
  - `date` (YYYY-MM-DD)
  - `category` (e.g., 2W/3W/4W)
  - `manufacturer`
  - `registrations` (integer)

Point the app to your file path via the **sidebar**.

## How YoY and QoQ are computed
- **YoY%**: `(Current value - Value 12 months ago) / (Value 12 months ago) * 100`
- **QoQ%**: `(Current value - Value 3 months ago) / (Value 3 months ago) * 100`

These are computed separately for each category and manufacturer.

## Roadmap
- ✅ Synthetic data + working dashboard
- ☐ Selenium scraper (if legally permitted)
- ☐ SQLite storage + scheduled refresh
- ☐ EV vs ICE segmentation layer
- ☐ Share of category (SoC) by manufacturer
- ☐ Export insights to PDF/Slides

## Video Walkthrough (to add)
Record a short (≤5 min) screen capture explaining:
- What the dashboard does
- How to operate filters
- 1–2 key investor insights (e.g., emerging momentum in 2W EV makers)

## Legal
Use data responsibly and review any terms/robots policy of data sources you scrape.
