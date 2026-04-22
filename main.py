from src.data_loader import load_all_data
from src.preprocessing import preprocess_trader_data, preprocess_sentiment_data, merge_data
from src.feature_engineering import finalize_features
from src.analysis import run_analysis
from src.model import run_model

def main():
    # Load
    trader_df, sentiment_df = load_all_data()

    # Preprocess
    trader_df = preprocess_trader_data(trader_df)
    sentiment_df = preprocess_sentiment_data(sentiment_df)

    # Merge
    df = merge_data(trader_df, sentiment_df)

    # Analysis
    run_analysis(df)

    # ML
    X, y = finalize_features(df)
    run_model(X, y)

if __name__ == "__main__":
    main()
    