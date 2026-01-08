def compute_correlation(df, cols=["budget","gross","votes"]):
    """Return correlation between key columns"""
    return df[cols].corr()
