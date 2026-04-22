import pandas as pd

def create_target(df):
    df['profit'] = (df['Closed PnL'] > 0).astype(int)

    return df

def select_features(df):
    df = df[['value', 'Size USD', 'Execution Price', 'Side', 'classification', 'profit']]

    return df
    
def encode_features(df):
    df = pd.get_dummies(df, columns=['Side', 'classification'], drop_first=True)
    
    return df

def finalize_features(df):
    df = df.copy()
    df = create_target(df)
    df = select_features(df)
    df = encode_features(df)

    df = df.dropna()

    X = df.drop('profit', axis=1)
    y = df['profit']

    return X, y
