# Linear Regression on Housing Prices

This project implements a linear regression model to predict housing prices based on features such as living area and number of bathrooms. The dataset contains 4,140 observations with both numerical and categorical features.

## Project Structure

```
├── data/                   # Contains the housing dataset
├── models/                 # Saved model artifacts
├── outputs/                # Generated plots (EDA and model evaluation)
├── Codveda_Linear_Regression.ipynb   # Main notebook
├── load.py                # Script for loading data or model
└── README.md              # Project overview (this file)
```

## Goals

- Explore the distribution of housing prices
- Clean and preprocess the dataset
- Apply log transformation to reduce skewness in the target variable
- Build and evaluate a linear regression model
- Visualize residuals and assess assumptions (linearity, homoscedasticity, normality)

## Key Features Used

- `sqft_living`
- `bathrooms`
- `log_price` as the target variable

## Evaluation

- R² score: (included in notebook)
- Residual analysis
- Actual vs Predicted plots
- Homoscedasticity check
- Final model saved to: `models/final_model.pkl`

## How to Run

1. Clone the repository
2. Install dependencies (see below)
3. Open the notebook and run all cells

## Installation

Install required packages:

```bash
pip install -r requirements.txt
```

## Author

Codveda Internship Task — Linear Regression