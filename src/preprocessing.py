import pandas as pd

def preprocess_trader_data(trader_df):
    trader_df['Timestamp IST'] = pd.to_datetime(
        trader_df['Timestamp IST'],
        errors='coerce'
    )

    print(f"Null Timestamp Values: {trader_df['Timestamp IST'].isnull().sum()}")

    trader_df = trader_df.dropna(subset=['Timestamp IST'])

    trader_df['date'] = trader_df['Timestamp IST'].dt.date

    trader_df['Closed PnL'] = pd.to_numeric(trader_df['Closed PnL'], errors='coerce')
    trader_df['Size USD'] = pd.to_numeric(trader_df['Size USD'], errors='coerce')
    trader_df['Execution Price'] = pd.to_numeric(trader_df['Execution Price'], errors='coerce')

    trader_df = trader_df.dropna(subset=['Closed PnL'])

    return trader_df

def preprocess_sentiment_data(sentiment_df):
    if 'Date' in sentiment_df.columns:
        sentiment_df.rename(columns={'Date': 'date'}, inplace=True)

    sentiment_df['date'] = pd.to_datetime(
        sentiment_df['date'],
        errors = 'coerce'
    )

    sentiment_df = sentiment_df.dropna(subset = ['date'])

    sentiment_df['date'] = sentiment_df['date'].dt.date

    sentiment_df['classification'] = sentiment_df['classification'].str.strip().str.lower()

    sentiment_df['value'] = pd.to_numeric(sentiment_df['value'], errors='coerce')

    return sentiment_df

def merge_data(trader_df, sentiment_df):
    print(f"Before Merge - Trader Data: {trader_df.shape}, Sentiment Data: {sentiment_df.shape}")

    df = pd.merge(trader_df, sentiment_df, on='date', how='left')
    print(f"After Merge - Merged Data: {df.shape}")

    print(f"Null Classification Values: {df['classification'].isnull().sum()}")

    df = df.dropna(subset = ['classification'])

    print(f"Final Data Shape after cleaning: {df.shape}")
    
    return df
