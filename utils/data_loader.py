
import pandas as pd
from pathlib import Path

def load_data(path: str) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    df = pd.read_csv(path)
    # type hints
    df["date"] = pd.to_datetime(df["date"])
    df["registrations"] = df["registrations"].astype(int)
    return df
