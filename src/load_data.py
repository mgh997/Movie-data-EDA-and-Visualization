import pandas as pd

def load_data(path="data/movies.csv"):
    """Load the movies dataset"""
    return pd.read_csv(path)
