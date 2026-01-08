def summarize(df):
    """Quick summary statistics"""
    return df.describe()

def top_movies_by(df, column, n=10):
    """Return top n movies by a column (like gross, votes)"""
    return df.sort_values(by=column, ascending=False).head(n)
