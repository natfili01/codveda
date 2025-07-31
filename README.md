# Codveda Data Science Internship Projects

This repository contains three data science projects completed as part of the **Codveda Internship Program (2025)**. The tasks span multiple levels and techniques, including regression, classification, and time-series forecasting using both classical and deep learning approaches.

##  Repository Structure

```
codveda/
├── Task 1 Level 2/       # Linear Regression (Predictive Modeling)
├── Task 2 Level 2/       # Logistic Regression (Classification)
├── Task 1 Level 3/       # Time Series Forecasting (SARIMA & LSTM)
```

Each folder contains:
-  Jupyter notebook (`.ipynb`)
-  Task-specific README.md
-  `data/`, `models/`, and `outputs/` subfolders
-  `requirements.txt`

---

##  Tasks Overview

###  Task 1 Level 2 — Linear Regression
**Objective:** Build and evaluate a regression model to predict housing prices.  
**Tools:** `scikit-learn`, `pandas`, `matplotlib`  
**Key steps:**
- Feature selection and engineering
- Model training and evaluation (MSE, R²)
- Visualization and interpretation

 Folder: [`Task 1 Level 2`](./Task%201%20Level%202)

---

###  Task 2 Level 2 — Logistic Regression Classification
**Objective:** Predict customer subscription to a term deposit (binary classification).  
**Tools:** `LogisticRegression`, `SMOTE`, `ROC AUC`, `confusion_matrix`  
**Highlights:**
- One-hot encoding of categorical variables
- Feature testing and selection based on ROC AUC
- Oversampling and final model evaluation

 Folder: [`Task 2 Level 2`](./Task%202%20Level%202)

---

###  Task 1 Level 3 — Time Series Forecasting (SARIMA & LSTM)
**Objective:** Forecast future stock prices using historical data.  
**Tools:** `statsmodels`, `SARIMAX`, `TensorFlow`, `LSTM`  
**Features:**
- Decomposition into trend, seasonality, residual
- SARIMA model with external regressors
- LSTM with lookback window and scaling

 Folder: [`Task 1 Level 3`](./Task%201%20Level%203)

---

##  How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/natfili01/codveda.git
   cd codveda
   ```

2. Create a virtual environment (optional but recommended)

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

---

##  Notes
- Each task has its own `requirements.txt`
- Models are saved under `models/` folder in each task
- Graphs, outputs, and reports are saved under `outputs/`

---

##  Author
**Nataliia Filipenko**  
B.Sc. Computer Science & AI, KPI  
GitHub: [@natfili01](https://github.com/natfili01)
