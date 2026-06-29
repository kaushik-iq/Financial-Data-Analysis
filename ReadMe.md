# 🏠 Household Income & Expenditure Analysis

## 📌 Project Overview

This project analyzes household income and expenditure data to identify spending patterns, income distribution, savings, and demographic trends. Using Python for data cleaning, exploratory data analysis (EDA), and visualization, the project provides meaningful business insights that can support financial planning and policy decisions.

---

## 🎯 Objectives

* Analyze the relationship between household income and expenditure.
* Compare spending behavior across different family types.
* Identify regional differences in income and expenses.
* Examine expenditure across different spending categories.
* Compare spending patterns among income quintiles.
* Analyze age-wise spending behavior.
* Estimate household savings.
* Generate meaningful business insights from the data.

---

## 📂 Dataset Information

The dataset contains **13,260 records** and includes household demographic, income, and expenditure information.

### Dataset Columns

| Column Name                                      | Description                |
| ------------------------------------------------ | -------------------------- |
| REF_DATE                                         | Reference year             |
| GEO                                              | Geographic region          |
| Statistic                                        | Statistical measure        |
| Before-tax household income quintile             | Income group before tax    |
| Household expenditures, summary-level categories | Expense category           |
| UOM                                              | Unit of measurement        |
| COORDINATE                                       | Dataset coordinate         |
| Expense                                          | Household expenditure      |
| Family type                                      | Household family structure |
| Age of older adult                               | Age group                  |
| Family income                                    | Income category            |
| Income                                           | Household income           |

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

### 1. Income vs Expenditure Analysis

* Scatter Plot
* Correlation Heatmap
* Average Income by Quintile
* Average Expense by Quintile

### 2. Family Type Spending Pattern

* Average Expense by Family Type
* Box Plot
* Bar Chart

### 3. Geographic Analysis

* Average Income by Region
* Average Expense by Region
* Highest Spending Regions

### 4. Expense Category Analysis

* Total Expense by Category
* Top Spending Categories
* Pie Chart
* Bar Chart

### 5. Income Quintile Comparison

* Pivot Table
* Stacked Bar Chart

### 6. Age-wise Spending Behaviour

* Average Expense by Age Group
* Heatmap
* Line Chart

### 7. Savings Analysis

Savings were estimated using:

```python
Savings = Income - Expense
```

Analysis includes:

* Average Savings by Income Quintile
* Average Savings by Family Type

---

## 📈 Business Insights

* Higher-income households generally spend more but also save more.
* Family type significantly influences household expenditure.
* Some regions have considerably higher average income and spending.
* Housing and food represent the largest expenditure categories.
* Spending patterns vary across income quintiles.
* Age groups show different spending priorities.
* Savings differ substantially across household types.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Household-Income-Analysis.git
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter notebook
```

---

## 📦 Required Libraries

```text
pandas
numpy
matplotlib
seaborn
jupyter
```

---

## 📊 Sample Business Questions Answered

* Do higher-income households spend more?
* Which family type spends the most?
* Which regions have the highest average income?
* Which regions have the highest household expenditure?
* What are the highest expenditure categories?
* Which income quintile saves the most?
* How does spending differ across age groups?

---

## 📌 Future Improvements

* Build an interactive Power BI dashboard.
* Develop a Streamlit web application.
* Apply machine learning models to predict household expenditure.
* Create regional expenditure forecasting models.
* Perform advanced statistical analysis.

---

## 👨‍💻 Author

**Shyam Yadav**

* Aspiring Data Analyst
* Machine Learning Enthusiast
* Python | SQL | Power BI | Pandas | NumPy | Matplotlib | Seaborn

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
s
