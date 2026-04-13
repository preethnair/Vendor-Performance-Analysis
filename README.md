# 📊 Vendor Performance Analysis & Dashboard

## 📌 Overview

This project is a **complete end-to-end data analytics pipeline** built to analyze vendor performance, optimize procurement decisions, and generate actionable business insights.

It covers:

* Data ingestion from CSV → SQL database
* Data transformation & feature engineering
* Exploratory Data Analysis (EDA)
* Business problem solving using analytics
* Statistical testing & confidence intervals
* Dashboard visualization for decision-making

---

## 🏗️ Project Architecture

```
CSV Files → Data Ingestion Script → SQLite Database → Data Transformation → EDA & Analysis → Dashboard
```

---

## ⚙️ Code Structure

### 🔹 Code 1: Data Ingestion (ETL Pipeline)

**Purpose:** Load raw CSV files into a structured SQL database.

#### Key Features:

* Reads multiple `.csv` files from a directory
* Stores data into **SQLite database (`inventory.db`)**
* Uses **SQLAlchemy engine**
* Implements **logging system** for monitoring

#### Highlights:

* Automated ingestion pipeline (can be scheduled)
* Logs execution time and ingestion status
* Converts raw files into structured database tables

---

### 🔹 Code 2: Data Transformation & Feature Engineering

**Purpose:** Create a consolidated **Vendor Summary Table**

#### Key Operations:

* SQL joins across:

  * `purchases`
  * `sales`
  * `vendor_invoice`
  * `purchase_prices`
* Data cleaning:

  * Fix data types
  * Handle missing values
  * Remove extra spaces
* Feature engineering:

  * **Gross Profit**
  * **Profit Margin**
  * **Stock Turnover**
  * **Sales-Purchase Ratio**

#### Output:

* Final table → `VendorSalesSummery`

---

### 🔹 Code 3: EDA & Business Insights

**Purpose:** Extract insights and solve real business problems

#### Key Analysis:

* Distribution plots & outlier detection
* Correlation heatmaps
* Data filtering for quality

---

## 📊 Business Problems Solved

### 1️⃣ Low Sales but High Margin Brands

* Identified brands needing **promotion or pricing adjustments**
* Strategy: Boost visibility to increase revenue

---

### 2️⃣ Top Performing Vendors & Brands

* Ranked vendors and brands based on **total sales**
* Helps in identifying key revenue drivers

---

### 3️⃣ Vendor Contribution Analysis (Pareto 80/20)

* Identified vendors contributing most to procurement
* Built **Pareto chart** for decision-making

---

### 4️⃣ Procurement Dependency

* Measured dependency on top vendors
* Helps mitigate **supply chain risk**

---

### 5️⃣ Bulk Purchasing Impact

* Found that **larger orders reduce unit cost significantly**
* Supports bulk purchasing strategy

---

### 6️⃣ Inventory Efficiency

* Detected vendors with **low stock turnover**
* Identified slow-moving inventory

---

### 7️⃣ Unsold Capital Analysis

* Calculated total **capital locked in inventory**
* Identified vendors contributing most to inefficiency

---

### 8️⃣ Statistical Analysis

#### ✔ Confidence Intervals

* Compared **profit margins** of:

  * Top-performing vendors
  * Low-performing vendors

#### ✔ Hypothesis Testing

* Used **T-test**
* Result: Significant difference in profit margins

---

## 📈 Dashboard

The final output is a **Vendor Performance Dashboard** providing:

* 💰 Total Sales, Purchases, Profit, Margin
* 📊 Purchase Contribution %
* 🏆 Top Vendors & Brands
* ⚠️ Low Performing Vendors & Brands
* 📉 Sales vs Profitability scatter analysis

### Key Insights from Dashboard:

* Few vendors dominate procurement (Pareto effect)
* High-margin brands often have low sales → opportunity zone
* Significant capital is locked in unsold inventory
* Strong variation in vendor performance

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Matplotlib, Seaborn**
* **SQLite**
* **SQLAlchemy**
* **SciPy (Statistical Testing)**

---

## 🚀 How to Run

```bash id="n1p2qs"
# Step 1: Install dependencies
pip install pandas numpy matplotlib seaborn sqlalchemy scipy

# Step 2: Run Data Ingestion
python data_ingestion.py

# Step 3: Create Vendor Summary
python vendor_summary.py

# Step 4: Run Analysis
python eda_analysis.py
```

---

## 📂 Output Files

* `inventory.db` → Database
* `VendorSalesSummery` → Final table
* `New_Vendor_Performance.csv` → Clean dataset
* `Logs/` → Execution logs

---

## 💡 Business Impact

This project enables:

* 📉 Reduction in unsold inventory
* 💰 Improved pricing & procurement strategy
* 📊 Data-driven vendor selection
* ⚡ Better supply chain optimization

---

## 📌 Conclusion

This is a **production-style analytics project** demonstrating:

* Real-world ETL pipeline
* SQL + Python integration
* Advanced EDA & statistical analysis
* Business-focused insights

👉 Ideal for **Data Analyst / Data Science portfolios**

---
