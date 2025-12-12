# Machine-Learning Projects

This repository contains a collection of Machine Learning projects developed as part of an advanced analytics curriculum. The projects demonstrate a progression in complexity, covering exploratory analysis, predictive modeling, dimensionality reduction, and model evaluation using real-world datasets.

Currently included projects:

- **BarcelonaMotorIBEX** – Predictive modeling of NO₂ pollution levels using regularized regression.
- **Vacaciones** – Classification of user travel preferences using linear and Bayesian models.
- **NASDAQ** – Financial forecasting using Neural Networks (MLP) and hyperparameter tuning.

---

## 📂 Repository Structure

Each folder includes the main notebook (or Python script), generated figures, and supporting resources required to reproduce the analysis.

---

## 🔷 Projects Overview

### **1. BarcelonaMotorIBEX** (Regression & Feature Engineering)
A predictive study analyzing daily **NO₂ levels in l’Eixample (Barcelona)** using open data from the city (2022–2024). The dataset includes vehicle registrations, mobility counts, electricity prices, traffic volume, and meteorological variables.

**Key Techniques:**
- Train/Test split (60/40) and detailed EDA.
- Data transformation and feature preprocessing.
- Dimensionality reduction (PCA) visualization.
- Models: **Linear Regression, Ridge Regression, LASSO**.
- **Statistical Significance:** Analysis using OLS (statsmodels) to identify redundant variables.
- **Feature Engineering:** Expansion with `PolynomialFeatures` (interaction terms) to capture non-linear relationships.
- Residual analysis and comparison of improved models.

### **2. Vacaciones** (Classification & Imbalance Handling)
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

### **3. NASDAQ** (Neural Networks for Regression)
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
- **Machine Learning:** Scikit-Learn (SVM, MLP, Trees, Linear Models)
- **Statistics:** Statsmodels
- **Data Loading:** apafib (Custom library for datasets)