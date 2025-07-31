# Time Series Forecasting for Stock Symbol 'D'

This project is part of the Codveda Data Science Internship (Level 3 — Task 1) and focuses on time series modeling and forecasting using traditional statistical and deep learning techniques.

---

## Objective

Forecast future stock prices for the symbol **'D'** by analyzing historical closing price data. The project evaluates different forecasting models including:

- SARIMA
- SARIMAX (with day-of-week exogenous features)
- LSTM Neural Network

---

## Project Highlights

### Data Preprocessing
- Filtered dataset for a single stock symbol (`'D'`)
- Set datetime index and ensured daily frequency with interpolation
- Created exogenous variables (e.g., day of the week) for SARIMAX

### Trend Smoothing
- 7-day Simple Moving Average (SMA)
- Simple Exponential Smoothing (SES)

### Stationarity Check
- Augmented Dickey-Fuller Test (ADF)
- Rolling mean and standard deviation visualization

### Time Series Models
#### SARIMA
- Model: (1, 0, 1) x (1, 1, 0, 7)
- Manual differencing applied
- Evaluated over 14-day forecast

#### SARIMAX
- Added one-hot encoded weekday features
- Evaluated on both 14-day forecast and 7-day prediction
- Also included 1-day prediction vs actual

#### LSTM Neural Network
- Lookback window: 30 days
- Recursive forecasting and walk-forward validation
- Model trained and saved for each fold

---

## Model Evaluation

| Model     | Horizon | RMSE    | MAE     |
|-----------|---------|---------|---------|
| SARIMA    | 14 days | 0.09811 | 0.07963 |
| SARIMAX   | 14 days | 0.01074 | 0.00687 |
| SARIMAX   | 7 days  | 0.00198 | 0.00126 |
| SARIMAX   | 1 day   | 0.00701 | 0.00701 |
| LSTM (CV) | 1 day   | 0.00300 | 0.00233 |
| LSTM (last) | 1 day | $0.15   | ~0.18% error |

---

## Files Included

- `time_series_forecasting_D.ipynb` — Full notebook with code and analysis
- `lstm_fold_1.keras` to `lstm_fold_5.keras` — Saved LSTM models per fold
- `requirements.txt` — Python environment dependencies

---

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. (Optional) Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the notebook:
   ```
   jupyter notebook time_series_forecasting_D.ipynb
   ```

4. Run all cells sequentially to reproduce the analysis and forecasts.

---

## License

This project was completed as part of the Codveda Data Science Internship (Level 3). All datasets were used for educational purposes only.

---

## Final Model Comparison

| Model        | Horizon     | RMSE     | MAE      | Notes                                      |
|--------------|-------------|----------|----------|--------------------------------------------|
| SARIMA       | 14 days     | 0.09811  | 0.07963  | No exogenous features                      |
| SARIMAX      | 14-day pred | 0.00198  | 0.00126  | One-hot weekday as exog                    |
| SARIMAX      | 7-day pred  | 0.00164  | 0.00133  | Slightly better than 14-day horizon        |
| SARIMAX      | 1-day pred  | 0.00701  | 0.00701  | Actual vs predicted on last real value     |
| LSTM (CV)    | 1-day pred  | 0.00300  | 0.00233  | Cross-validated, walk-forward              |
| LSTM (final) | 1-day pred  | $0.15    | ~0.18%   | Forecasted next day price: $80.91          |
