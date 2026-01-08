import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(df, cols=None):
    """Show correlation heatmap for selected columns"""
    if cols is None:
        cols = df.select_dtypes(include="number").columns
    corr = df[cols].corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def plot_top_movies(df, column, n=10):
    """Bar plot for top n movies by a column"""
    top = df.sort_values(by=column, ascending=False).head(n)
    plt.figure(figsize=(10,6))
    sns.barplot(data=top, x=column, y="name")   # <-- changed 'title' to 'name'
    plt.title(f"Top {n} Movies by {column}")
    plt.show()

