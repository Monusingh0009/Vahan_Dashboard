# Vahan Investor Dashboard  

An interactive dashboard built using **Streamlit** and **Python** to analyze vehicle registration data from the **Vahan Dashboard**. It is designed with an investor’s perspective, highlighting category-wise and manufacturer-wise growth trends.  

---

## 🚀 Setup Instructions  

### 1. Clone the repository  
```bash
git clone <your-repo-url>
cd vahan_dashboard23
```

### 2. Create a virtual environment (recommended)  
```bash
python -m venv venv
source venv/bin/activate    # for Mac/Linux
venv\Scripts\activate       # for Windows
```

### 3. Install dependencies  
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app  
```bash
streamlit run app.py
```

### 5. Data Input  
- By default, the app loads a **sample CSV** stored in `data/registrations_sample.csv`.  
- You can replace this file with your own dataset (exported from Vahan Dashboard).  
- Alternatively, provide the path in the sidebar input.  

---

## 📊 Data Assumptions  

1. **Data Source**  
   - Data is scraped/exported from the **Vahan Dashboard**:  
     [Vahan Reports](https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml).  
   - Only **vehicle registrations** are considered, not renewals or deregistrations.  

2. **Date Handling**  
   - The dataset includes a `date` column with daily records.  
   - Date ranges in the dashboard are applied as filters (`start_date`, `end_date`).  
   - For **YoY and QoQ growth**, the app calculates percentage changes based on aggregated monthly/quarterly totals.  

3. **Categories**  
   - Vehicles are grouped as **2W, 3W, 4W** based on the `category` column.  
   - Assumes no missing category values; if missing, they are ignored.  

4. **Manufacturers**  
   - Manufacturer names are taken directly from the dataset.  
   - Assumes consistent naming (e.g., “Hero” vs “Hero MotoCorp” may cause duplicate entries if not standardized).  

5. **Sample Data**  
   - The provided sample CSV is synthetic (for demonstration).  
   - Real-world results may vary once live Vahan data is integrated.  
