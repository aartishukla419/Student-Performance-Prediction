# "NOVORA": Intelligent Learning Analytics and Student Success Prediction Framework


## 📌 Project Overview

The **Student Performance Prediction System** is a Machine Learning-based predictive analytics solution designed to estimate student academic performance using historical educational and behavioral attributes. The system leverages data-driven methodologies to identify patterns that influence academic outcomes and generate accurate performance predictions.

The project follows the complete Machine Learning Development Lifecycle, including problem understanding, data collection, preprocessing, exploratory analysis, feature engineering, model development, evaluation, and deployment.

---

# Phase 1: Problem Understanding

## 🎯 Objective

To develop an intelligent machine learning model capable of predicting student academic performance using various educational and behavioral indicators.

## 📖 Problem Statement

Educational institutions generate large volumes of student-related data on a regular basis. However, identifying students who may require additional academic support or intervention remains a challenging task.

By utilizing Machine Learning techniques, historical student records can be analyzed to uncover hidden patterns and predict future academic performance.

This project aims to build a predictive system that estimates student performance using factors such as:

* Weekly Self Study Hours
* Attendance Percentage
* Class Participation
* Academic Grade
* Historical Academic Records

## 🎯 Expected Outcome

The final solution should be capable of:

* Predicting student academic performance accurately.
* Supporting data-driven educational decisions.
* Assisting educators in identifying students requiring additional guidance.
* Improving overall academic monitoring and performance assessment.

---

# Phase 2: Data Collection

## 🎯 Objective

To collect, import, and understand the dataset that serves as the foundation for the machine learning pipeline.

## 📖 Overview

Data collection is the initial operational stage of every machine learning project. A comprehensive understanding of the dataset structure, quality, and attributes is essential before performing any analytical or modeling tasks.

The student performance dataset is imported and examined to understand its dimensions, feature composition, data types, and statistical characteristics.

## 🔍 Activities Performed

* Imported the dataset into the analytical environment.
* Verified successful dataset loading.
* Examined dataset dimensions and structure.
* Identified available attributes and feature types.
* Generated descriptive statistical summaries.
* Reviewed overall dataset composition and quality.

## 📦 Deliverables

* Dataset successfully imported.
* Dataset dimensions documented.
* Feature inventory established.
* Statistical summary generated.
* Initial dataset understanding completed.

## ✅ Outcome

A comprehensive understanding of the dataset has been established, providing the foundation for preprocessing, analysis, feature engineering, and predictive modeling.

---

# Phase 3: Data Preprocessing

## 🎯 Objective

To clean, transform, and prepare the dataset for machine learning model development.

## 📖 Overview

Real-world datasets often contain inconsistencies such as missing values, duplicate observations, outliers, and categorical attributes that require transformation before model training.

This phase focuses on improving dataset quality and ensuring that all features are suitable for machine learning algorithms.

## 🔍 Activities Performed

* Missing value assessment.
* Duplicate record identification.
* Outlier detection and analysis.
* Feature consistency validation.
* Categorical feature encoding.
* Numerical feature standardization.
* Dataset preparation for modeling.

## 📦 Deliverables

* Missing value report.
* Duplicate record assessment.
* Outlier analysis.
* Encoded categorical variables.
* Scaled numerical attributes.
* Clean machine-learning-ready dataset.

## ✅ Outcome

A structured, reliable, and analysis-ready dataset is generated for downstream machine learning tasks.

---

# Phase 4: Exploratory Data Analysis (EDA)

## 🎯 Objective

To discover patterns, trends, distributions, and relationships among variables within the dataset.

## 📖 Overview

Exploratory Data Analysis transforms raw data into meaningful insights through statistical techniques and visual exploration.

The objective is to understand how different educational factors influence student academic performance and identify relationships that may improve predictive modeling.

## 🔍 Activities Performed

### Univariate Analysis

* Feature distribution analysis.
* Frequency analysis.
* Statistical summary generation.

### Bivariate Analysis

* Feature-to-target relationship analysis.
* Comparative visualization.
* Pattern identification.

### Correlation Analysis

* Correlation matrix generation.
* Heatmap visualization.
* Dependency analysis among variables.

## 📊 Visualizations Generated

* Histograms
* Box Plots
* Scatter Plots
* Correlation Heatmaps
* Distribution Charts

## 📦 Deliverables

* Univariate Analysis Report
* Bivariate Analysis Report
* Correlation Analysis Report
* Statistical Insights
* Visual Interpretation Summary

## ✅ Outcome

A comprehensive understanding of dataset characteristics and feature interactions has been achieved, supporting feature engineering and model development.

---

# Phase 5: Feature Engineering

## 🎯 Objective

To improve model performance by selecting relevant features and eliminating unnecessary information.

## 📖 Overview

Feature Engineering transforms raw attributes into meaningful predictors that enhance machine learning performance.

The process focuses on identifying high-impact variables, reducing redundancy, and constructing an optimized training dataset.

## 🔍 Activities Performed

* Feature relevance assessment.
* Feature selection.
* Redundant attribute removal.
* Training dataset optimization.
* Final predictor preparation.

## 📦 Deliverables

* Feature Selection Report
* Feature Importance Analysis
* Optimized Feature Set
* Final Training Dataset

## ✅ Outcome

A refined dataset containing only meaningful predictive attributes is prepared for machine learning model development.

---

# Phase 6: Model Building

## 🎯 Objective

To train and compare multiple machine learning models for predicting student academic performance.

## 📖 Overview

Machine learning algorithms are trained on historical student data to learn underlying patterns and generate predictions on unseen observations.

Multiple regression models are implemented to identify the most effective predictive solution.

## 🤖 Models Implemented

### Linear Regression

A baseline regression model used for understanding linear relationships among variables.

### Decision Tree Regressor

A tree-based learning algorithm capable of capturing non-linear relationships.

### Random Forest Regressor

An ensemble learning technique that combines multiple decision trees to improve prediction accuracy and robustness.

## 🔍 Activities Performed

* Train-Test Split Creation.
* Model Training.
* Prediction Generation.
* Performance Benchmarking.
* Comparative Analysis.
* Final Model Selection.

## 📦 Deliverables

* Trained Linear Regression Model
* Trained Decision Tree Model
* Trained Random Forest Model
* Prediction Outputs
* Model Comparison Report

## ✅ Outcome

Multiple predictive models have been successfully trained and prepared for evaluation.

---

# Phase 7: Model Evaluation

## 🎯 Objective

To evaluate model performance and identify the most suitable model for deployment.

## 📖 Overview

Model evaluation measures the ability of machine learning algorithms to generate accurate predictions on previously unseen data.

Multiple regression performance metrics are utilized to benchmark and compare model effectiveness.

## 📏 Evaluation Metrics

### Mean Absolute Error (MAE)

Measures the average magnitude of prediction errors.

### Mean Squared Error (MSE)

Measures squared prediction errors.

### Root Mean Squared Error (RMSE)

Represents prediction error in the original target scale.

### R² Score

Measures the proportion of variance explained by the model.

## 🔍 Activities Performed

* Prediction evaluation.
* Metric computation.
* Comparative analysis.
* Visualization of model performance.
* Best model identification.

## 📦 Deliverables

* Model Evaluation Report
* Performance Metrics Summary
* Comparative Analysis Dashboard
* Best Model Selection

## ✅ Outcome

The highest-performing machine learning model is selected and prepared for deployment.

---

# Phase 8: Model Deployment

## 🎯 Objective

To deploy the trained machine learning model through an interactive web application for real-time predictions.

## 📖 Overview

Deployment transforms the machine learning solution into a practical application accessible to end users.

A Streamlit-based web application is developed to enable users to provide academic inputs and receive instant performance predictions.

## 🚀 Deployment Components

* Trained Machine Learning Model (.pkl)
* Streamlit Application
* Requirements File
* User Interface Components
* Prediction Engine
* Deployment Configuration

## 🖥 Application Features

* Interactive User Interface
* Real-Time Prediction Generation
* Academic Performance Dashboard
* Visualization Components
* User-Friendly Input Forms

## 📦 Deliverables

* Trained Model File
* Streamlit Application
* Deployment Package
* Requirements Configuration
* Live Deployment URL

## ✅ Outcome

A fully functional Student Performance Prediction System capable of generating real-time predictions through an interactive web interface has been successfully deployed.

---

# 🏆 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Plotly
* Streamlit
* Joblib

---

# 📈 Project Workflow

Dataset Collection

⬇️

Data Preprocessing

⬇️

Exploratory Data Analysis

⬇️

Feature Engineering

⬇️

Model Training

⬇️

Model Evaluation

⬇️

Model Selection

⬇️

Model Deployment

⬇️

Real-Time Prediction


## Team Members

 Aarti Shukla
 Pranavi Kashyap
 
