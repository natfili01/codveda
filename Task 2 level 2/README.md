# Codveda Internship Project — Logistic Regression

## 📌 Task
Build and evaluate a classification model using **logistic regression** to predict whether a bank client will subscribe to a term deposit.

Dataset: `bank-full.csv` (Bank Marketing Dataset)

## ✅ Workflow
1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering & One-Hot Encoding
4. Model Building using `LogisticRegression` (scikit-learn)
5. Evaluation using Accuracy, Precision, Recall, F1-score, ROC AUC
6. Model saving via `joblib`

## 📊 Final Model Metrics (example)
- **Accuracy:** 0.68
- **Precision (class 1):** 0.20
- **Recall (class 1):** 0.56
- **ROC AUC:** 0.67

## 💾 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/codveda-project.git
   cd codveda-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the notebook:
   ```bash
   jupyter notebook Codveda_Logistic_Model.ipynb
   ```

## 📂 File Structure
```
.
├── data/
│   └── bank-full.csv
├── models/
│   └── final_logistic_model.pkl
├── outputs/
│   └── roc_curve.png
├── Codveda_Logistic_Model.ipynb
├── requirements.txt
└── README.md
```

## 🔖 Author
Nataliia Filipenko — Codveda Internship 2025
