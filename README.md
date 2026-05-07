# Machine-Learning Projects

This repository contains a collection of Machine Learning projects developed as part of an advanced analytics curriculum. The projects demonstrate a progression in complexity, covering exploratory analysis, predictive modeling, dimensionality reduction, and model evaluation using real-world datasets.

Currently included projects:

- **LaLiga Goals Predictor** – Predicting total match goals using classification ensembles and unsupervised clustering.
- **BarcelonaMotorIBEX & aireLimpio** – Predictive modeling of NO₂ pollution levels using regularized regression.
- **Vacaciones** – Classification of user travel preferences using linear and Bayesian models.
- **NASDAQ** – Financial forecasting using Neural Networks (MLP) and hyperparameter tuning.

---

## 📂 Repository Structure

Each folder includes the main notebook (or Python script), generated figures, and supporting resources required to reproduce the analysis.

```text
Machine-Learning/
├── Explorator Projects/
│   ├── aireLimpio.py
│   ├── BarcelonaMotorIBEX.py
│   ├── NASDAQ.ipynb
│   └── Vacaciones.ipynb
├── LaLiga Goals Predictor/
│   ├── doc/
│   │   └── Docu_Predictor_Goals.pdf
│   └── src/
│       └── GoalPredictorLaLiga.ipynb
└── README.md

## 🔷 Projects Overview

### **1. LaLiga Goals Predictor** (Classification, Feature Engineering & Clustering)
A comprehensive study to predict the range of total goals (0-1, 2-3, 4+) in Spanish La Liga matches (2019-2025) relying exclusively on pre-match data. 

**Key Techniques:**
- **Feature Engineering:** Extraction of contextual metrics such as rolling averages for current form (Last-5), accumulated season statistics, and historical direct matchups (Head-to-Head).
- **Unsupervised Learning & EDA:** Dimensionality reduction via PCA and t-SNE. Implemented K-Means clustering (k=3) to extract tactical latent structures (defensive, vulnerable, offensive profiles) and integrated cluster assignments/distances as new predictive features.
- **Predictive Modeling:** Benchmarking of linear models (Logistic Regression, SVM) against non-linear ensembles (Random Forest, Gradient Boosting, SVM RBF).
- **Validation Protocol:** Strict chronological Train/Test split (Train: 2019-2023, Test: 2024-2025) to simulate production environments and prevent future data leakage.
- **Interpretability:** Selection of Random Forest as the final model. Feature importance analysis revealed local defensive solidity (`home_ga_total`) and historical rivalry (`h2h_goals`) as the primary drivers over pure offensive metrics.

### **2. aireLimpio** (Regression & Feature Engineering)
A predictive study analyzing daily **NO₂ levels in l’Eixample (Barcelona)** using open data from the city (2022–2024). The dataset includes vehicle registrations, mobility counts, electricity prices, traffic volume, and meteorological variables ingested via the `apafib` library (`load_BCN_NO2`).

**Key Techniques:**
- Train/Test split (60/40) and detailed EDA.
- Data transformation and feature preprocessing.
- Dimensionality reduction (PCA) visualization.
- Models: **Linear Regression, Ridge Regression, LASSO**.
- **Statistical Significance:** Analysis using OLS (statsmodels) to identify redundant variables.
- **Feature Engineering:** Expansion with `PolynomialFeatures` (interaction terms) to capture non-linear relationships.
- Residual analysis and comparison of improved models.

### **3. BarcelonaMotorIBEX** (Financial Data Ingestion & EDA)
Data extraction and exploratory pipeline for the **IBEX 35** financial index and related local indicators in Barcelona, utilizing the `apafib` library (`load_BCN_IBEX`).

**Key Techniques:**
- Automated data retrieval and DataFrame structuring using Pandas/NumPy.
- Pre-modeling exploratory data analysis (EDA).

### **4. Vacaciones** (Classification & Imbalance Handling)
A classification project involving user ratings for travel categories (parks, theaters, beaches, etc.) to predict user profiles.

**Key Techniques:**
- Exploratory analysis and correlation study.
- Handling slight class imbalance using `class_weight='balanced'`.
- Models:
  - **Gaussian Naive Bayes** (with Gaussianization of features).
  - **Linear Discriminant Analysis (LDA)**.
  - **Logistic Regression** with extensive hyperparameter tuning.
- **Evaluation:** Cross-validation, Accuracy, F1-score, and ROC–AUC curves.
- Interpretation of model coefficients to understand feature importance per class.

### **5. NASDAQ** (Neural Networks for Regression)
An advanced project focused on predicting stock market indices using **Multi-Layer Perceptrons (MLP)**. This project shifts focus from linear models to non-linear deep learning architectures.

**Key Techniques:**
- **Data Scaling:** Implementation of `MinMaxScaler`/`StandardScaler` (critical for Neural Network convergence).
- **Model:** **MLPRegressor** (Scikit-Learn).
- **Architecture Search:** Exploration of different hidden layer configurations (depth vs. width).
- **Hyperparameter Tuning:** Grid search for activation functions (`relu`, `tanh`), solvers (`adam`, `sgd`), and regularization (`alpha`).
- **Diagnostics:** Analysis of **Loss Curves** (Training vs. Validation loss) to detect overfitting or underfitting.
- Comparison of the Neural Network performance against linear baselines.

---

## 🛠️ Technologies Used

- **Core:** Python 3, NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn (SVM, MLP, Trees, Linear Models, K-Means)
- **Statistics:** Statsmodels
- **Data Loading:** apafib (Custom library for datasets)