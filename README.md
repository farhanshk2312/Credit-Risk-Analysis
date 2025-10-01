# Credit Risk Analysis Project

## Introduction

Financial institutions face significant challenges in assessing loan applicants’ creditworthiness. The ability to predict defaults and repayment behavior is critical for risk management, profitability, and compliance. This project leverages modern data platforms such as Google BigQuery and Databricks to build a scalable pipeline for credit risk analysis. By applying data preprocessing, feature engineering, and advanced analytics, the aim is to extract insights that improve decision-making in lending.

## Data Overview

Source: https://www.kaggle.com/datasets/rameshmehta/credit-risk-analysis

The dataset contains complete loan data for all loans issued through the year 2007 - 2015, including the current loan status (Current, Late, Fully Paid, etc.) and latest payment information. It contains total of 8,55,969 records with 73 features including target variable. 

Moreover, the dataset is very unbalanced, with approximately 6 % of loans considered as defaulted. This dataset has different types of features such as categorical, numeric & date. Some important features:


  (1) Borrower information: employment length, annual income, debt-to-income ratio
  
  
  (2) Loan details: loan amount, issue date, interest rate, installment, term
  
  
  (3) Credit history: delinquency status, revolving utilization, credit line information
  
  
  (4) Repayment status: loan status (fully paid, default, charged off, etc.)


The dataset was initially into in BigQuery, serving as the raw data source, and was later ingested into Databricks Catalog for transformation and analysis.



## Objectives

(1) Data Management: Establish a clean pipeline for moving data from BigQuery to Databricks.


(2) Preprocessing: Handle missing values, standardize date formats, and normalize data types.


(3) Feature Engineering: Create derived variables to capture borrower behavior and loan performance patterns.


(4) Exploratory Data Analysis (EDA): Summarize key statistics and uncover trends.


(5) Risk Modeling Readiness: Prepare the data for future predictive modeling (e.g., default prediction, repayment probability).


## Approach

1. Data Storage & Ingestion

      Raw loan data stored in BigQuery.
    
      Connected Databricks to BigQuery and loaded raw tables into Databricks Catalog.


2. Data Parsing

    Converted string-based dates (e.g., issue_d) into proper DATE fields using to_date.
    
    Standardized inconsistent formats across different timestamp columns.


3. Handling Missing Values

    Identified missing data via summary statistics.
    
    Applied context-specific strategies:

    Categorical fields: replaced with "Unknown" or grouped as a new category.
    
    Numerical fields: replaced with 0, median, or imputed where necessary.
    
    Date fields: left null when parsing failed (retained missingness as an informative feature).
   

5. Feature Engineering

    Revolving Utilization = revol_bal / total_rev_hi_lim.
    
    Loan-to-Income Ratio = loan_amnt / annual_inc.
    
    Loan Age = current_date - issue_d.
    
    Default Risk Interactions = e.g., default_flag * int_rate.
    
    Categorical transformations: employment length categories, payment status (pending vs. no further payments).
   

5. Deep Analysis

    Performed EDA on distributions of loan amounts, interest rates, income levels, and default rates.
    
    Identified correlations between borrower attributes and loan performance.
    
    Segmented risk patterns across different borrower groups (e.g., high income vs. low income, short vs. long employment).



This project successfully established a data pipeline from BigQuery into Databricks Unity Catalog, enabling systematic data preprocessing, cleaning, and enrichment. The curated dataset is now ready for advanced predictive modeling, enabling stakeholders to assess creditworthiness, minimize defaults, and optimize lending strategies.


## Next Steps

(1) Exploratory Modeling

  Implement baseline models (e.g., Logistic Regression) to predict loan default.
  
  Compare with tree-based methods like Random Forest and Gradient Boosting (XGBoost/LightGBM).


(2) Feature Selection & Scaling

  Evaluate feature importance (SHAP values, gain importance).
  
  Standardize numerical variables where appropriate.


(3) Model Evaluation

  Use ROC-AUC, Precision-Recall, and F1-score to assess predictive performance.
  
  Validate models using cross-validation and test sets.


(4) Deployment & Monitoring

  Deploy the final model in Databricks MLflow for tracking and serving.
  
  Set up monitoring for model drift and performance degradation.
