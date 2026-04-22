def run_analysis(df):
    print("\n=== Average PnL by Sentiment ===")
    print(df.groupby('classification')['Closed PnL'].mean().sort_values())

    print("\n=== Trade Count by Sentiment ===")
    print(df['classification'].value_counts())

    print("\n=== PnL by Side ===")
    print(df.groupby('Side')['Closed PnL'].mean())

    print("\n=== PnL by Sentiment & Side ===")
    print(df.groupby(['classification', 'Side'])['Closed PnL'].mean())
