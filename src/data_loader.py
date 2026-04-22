import pandas as pd

def load_trader_data(path):
    try:
        trader_df = pd.read_csv(path)
    except Exception as e:
        print(f"Error loading trader data: {e}")
        return None
    return trader_df

def load_sentiment_data(path):
    try:
        sentiment_df = pd.read_csv(path)
    except Exception as e:
        print(f"Error loading sentiment data: {e}")
        return None
    return sentiment_df

def load_all_data():
    trader_data_path = 'data/historical_data.csv'
    sentiment_data_path = 'data/fear_greed_index.csv'

    trader_df = load_trader_data(trader_data_path)
    sentiment_df = load_sentiment_data(sentiment_data_path)
    
    if trader_df is None or sentiment_df is None:
        print("Failed to load data.")
    else:
        print(f"Trader Data : {trader_df.shape} \nSentiment Data : {sentiment_df.shape}")
        print(f"Trader Data Preview: {trader_df.head(2)} \nSentiment Data Preview : {sentiment_df.head(2)}")
    
    return trader_df, sentiment_df
