import pandas as pd

def clean_data(df):
    """Basic cleaning: remove duplicates and missing values for key columns"""
    df = df.copy()
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["budget", "gross", "votes"], inplace=True)
    # convert to numeric if needed
    df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
    df["gross"] = pd.to_numeric(df["gross"], errors="coerce")
    return df
