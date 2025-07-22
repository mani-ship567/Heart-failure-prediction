"""Data loading utilities."""
import pandas as pd
from pathlib import Path
from .config import DATA_PATH, TARGET_COL

def load_data(path: str | None = None) -> pd.DataFrame:
    path = path or DATA_PATH
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    df = pd.read_csv(path)
    return df

def split_xy(df):
    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]
    return X, y
