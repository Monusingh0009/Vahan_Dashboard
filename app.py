
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data
from utils.metrics import compute_periods, agg_category, agg_manufacturer, between_dates

st.set_page_config(page_title="Vahan Investor Dashboard", layout="wide")

st.title("Vehicle Registration Trends — Investor Dashboard")

with st.sidebar:
    st.header("Controls")
   
    
    df = load_data("data/registrations_sample.csv")
    df = compute_periods(df)

    min_d, max_d = df["date"].min(), df["date"].max()
    # start, end = st.date_input("Date range", value=(min_d, max_d), min_value=min_d, max_value=max_d)col1, col2 = st.columns(2)
    
    col1, col2 = st.columns(2)
    with col1:
      start = st.date_input(
        "Start date",
        value=min_d,
        min_value=min_d,
        max_value=max_d
      )

    with col2:
       end = st.date_input(
        "End date",
        value=max_d,
        min_value=min_d,
        max_value=max_d
       )
    df = between_dates(df, start, end)

    categories = sorted(df["category"].unique().tolist())
    selected_cats = st.multiselect("Vehicle categories", categories, default=categories)

    manufacturers = sorted(df["manufacturer"].unique().tolist())
    selected_mans = st.multiselect("Manufacturers", manufacturers, default=manufacturers)

    # Filter
    df = df[df["category"].isin(selected_cats) & df["manufacturer"].isin(selected_mans)]

tab1, tab2 = st.tabs(["Category view", "Manufacturer view"])

with tab1:
    st.subheader("Total vehicles by category")
    cat = agg_category(df)
    col1, col2 = st.columns(2)
    with col1:
        st.caption("Monthly trend")
        fig = px.line(cat, x="date", y="registrations", color="category", markers=True)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.caption("YoY % and QoQ % — last available month")
        last = cat.sort_values("date").groupby("category").tail(1)
        last = last[["category","registrations","yoy_%","qoq_%"]].sort_values("registrations", ascending=False)
        st.dataframe(last.set_index("category"))

with tab2:
    st.subheader("Each manufacturer")
    man = agg_manufacturer(df)
    # KPI for top manufacturers in selection by latest month
    latest = man.sort_values("date").groupby(["category","manufacturer"]).tail(1)
    st.caption("Latest month KPIs")
    st.dataframe(latest.sort_values("registrations", ascending=False).reset_index(drop=True))

    pick_cat = st.selectbox("Pick a category for charts", sorted(df["category"].unique()))
    mcat = man[man["category"] == pick_cat]

    col1, col2 = st.columns(2)
    with col1:
        st.caption(f"{pick_cat}: Manufacturer trends")
        fig = px.line(mcat, x="date", y="registrations", color="manufacturer", markers=True)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.caption("YoY % change (by manufacturer)")
        fig2 = px.line(mcat, x="date", y="yoy_%", color="manufacturer", markers=True)
        st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.markdown("**Investor quick take:**")
st.markdown(
    "- Track category momentum via YoY% for structural growth, and QoQ% for near-term acceleration.\n"
    "- Use the filters to isolate EV-heavy brands (e.g., Ather) versus legacy leaders to see share shifts."
)

st.caption("Note: This app ships with synthetic data. Replace `data/registrations_sample.csv` with your scraped export to go live.")
