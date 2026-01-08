from src.load_data import load_data
from src.clean_data import clean_data
from src.eda import summarize, top_movies_by
from src.visualization import plot_correlation_matrix, plot_top_movies
from src.analysis import compute_correlation

def main():
    # load & clean
    df = load_data()
    df = clean_data(df)

    # summaries & insights
    print("Summary statistics:\n", summarize(df))
    print("\nTop 10 movies by gross revenue:\n", top_movies_by(df, "gross"))

    # correlations
    print("\nCorrelation matrix:\n", compute_correlation(df))

    # plots
    plot_correlation_matrix(df)
    plot_top_movies(df, "gross")
    plot_top_movies(df, "votes")

if __name__ == "__main__":
    main()
