
import pandas as pd

def compute_periods(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["quarter_label"] = df["date"].dt.to_period("Q").astype(str)
    return df

def yoy_change(series: pd.Series) -> pd.Series:
    return series.pct_change(periods=12) * 100

def qoq_change(series: pd.Series) -> pd.Series:
    # Quarter over quarter: change with lag=3 months
    return series.pct_change(periods=3) * 100

def agg_category(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby(["date","category"], as_index=False)["registrations"].sum()
    g["yoy_%"] = yoy_change(g.groupby("category")["registrations"].transform(lambda s: s))
    g["qoq_%"] = qoq_change(g.groupby("category")["registrations"].transform(lambda s: s))
    return g

def agg_manufacturer(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby(["date","category","manufacturer"], as_index=False)["registrations"].sum()
    # compute by (category, manufacturer)
    g["yoy_%"] = g.groupby(["category","manufacturer"])["registrations"].apply(yoy_change).reset_index(level=[0,1], drop=True)
    g["qoq_%"] = g.groupby(["category","manufacturer"])["registrations"].apply(qoq_change).reset_index(level=[0,1], drop=True)
    return g

def between_dates(df: pd.DataFrame, start_date, end_date):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    mask = (df["date"] >= pd.to_datetime(start_date)) & (df["date"] <= pd.to_datetime(end_date))
    return df.loc[mask]
