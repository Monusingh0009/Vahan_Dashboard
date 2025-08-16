
"""
Scraping template for Vahan Dashboard (manual/automated).

IMPORTANT: Check terms of service and robots.txt and comply with local laws and site policies.
If scraping is disallowed, consider manual export or official data sources.

Two approaches:

1) Manual export workflow
-------------------------
- Use the Vahan Dashboard filters to select date range, category, and manufacturer tables.
- Copy table(s) to CSV using your browser (or print to CSV with a table clipper extension).
- Save as `data/registrations.csv` with columns:
  date, category, manufacturer, registrations

2) Automated scraping (if permitted)
------------------------------------
- Use Selenium because the dashboard is JS-rendered.
- Pseudocode:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    driver.get("https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml")
    # interact with filters, wait for table, iterate pages, collect rows
    # write to CSV with columns above

Once you have the CSV, point the Streamlit app to the file path in the sidebar.
"""
