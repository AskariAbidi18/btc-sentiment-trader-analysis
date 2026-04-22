# Bitcoin Market Sentiment vs Trader Performance

## Objective

This project analyzes the relationship between Bitcoin market sentiment (Fear & Greed Index) and trader performance using historical trading data. The goal is to uncover patterns in profitability across different sentiment regimes and evaluate whether sentiment can help predict trade outcomes.

---

## Datasets

1. **Historical Trader Data (Hyperliquid)**
   - Contains trade-level information including execution price, size, side (BUY/SELL), and realized profit/loss (Closed PnL).

2. **Bitcoin Fear & Greed Index**
   - Daily sentiment classification (Extreme Fear → Extreme Greed)
   - Numerical sentiment score (0–100)

---

## Methodology

### 1. Data Preprocessing
- Converted timestamps to datetime and aligned both datasets on a daily basis
- Extracted date from trade timestamps for merging
- Cleaned numerical columns (PnL, size, price)
- Merged trader data with sentiment data using date as the key
- Removed rows with missing sentiment data

### 2. Exploratory Data Analysis
- Analyzed average PnL across sentiment categories
- Evaluated trading activity distribution across sentiment regimes
- Compared BUY vs SELL performance
- Examined PnL variability under different market conditions

### 3. Feature Engineering
- Created binary target variable:  
  **Profit = 1 if Closed PnL > 0, else 0**
- Selected key features:
  - Sentiment value
  - Trade size (USD)
  - Execution price
  - Trade side
  - Sentiment classification
- Applied one-hot encoding for categorical variables

### 4. Model
- Trained a **Random Forest Classifier** to predict trade profitability
- Evaluated using accuracy and classification metrics
- Extracted feature importance to understand key drivers

---

## Results

### Model Performance
- Accuracy: **94.0%**
- Balanced precision and recall across profitable and non-profitable trades

### Feature Importance (Top Drivers)
1. Execution Price (~53%)
2. Trade Size (~20%)
3. Sentiment Value (~15%)
4. Trade Side (SELL)
5. Sentiment Categories (minor contribution)

---

## Key Insights

1. **Profitability increases with bullish sentiment**
   - Trades executed during Greed and Extreme Greed phases yield significantly higher average PnL compared to Fear phases.

2. **Extreme Greed presents high-reward conditions**
   - Highest observed profitability occurs during Extreme Greed, particularly for SELL trades, indicating strong directional opportunities.

3. **Trader behavior varies across sentiment regimes**
   - BUY trades perform better during Fear phases
   - SELL trades dominate during Greed phases

4. **Trade characteristics outweigh sentiment labels**
   - Execution price and trade size are the strongest predictors of profitability
   - Numerical sentiment value is more informative than categorical labels

5. **Market extremes increase volatility**
   - Both Extreme Fear and Extreme Greed exhibit higher variability in returns, indicating elevated risk conditions

---

## Limitations

- Significant data loss occurred during preprocessing due to timestamp inconsistencies and missing sentiment alignment
- Model performance may be influenced by class imbalance and simplified feature set
- Results are based on historical data and may not generalize across all market conditions

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

---

## Conclusion

This analysis demonstrates a clear relationship between market sentiment and trading performance. While sentiment alone is not the strongest predictor, it provides meaningful context when combined with trade-level features. The results suggest that integrating sentiment signals into trading strategies can improve decision-making, particularly during extreme market conditions.

---
