# 🛠️ Sales Data ETL and Analysis Pipeline

This project simulates a complete data pipeline for sales data, covering the full ETL process, data cleaning, business metrics generation, and visualization using Python.

---

## 📌 Project Overview

The goal of this project is to demonstrate core skills in **Data Engineering** and **Data Analysis** using tools like:
- **Python**, **Pandas**
- **Excel / CSV**
- **Matplotlib / Seaborn**
- (Optional: Power BI for dashboarding)

---

## 🔄 ETL Pipeline

### ✅ **Extract**
- Simulated dataset (`base_vendas_projeto1.xlsx`) containing 500 sales records.
- Columns include: Date, Product, Region, Seller, Quantity, Unit Price, Unit Cost.

### 🔧 **Transform**
- Data cleaning:
  - Removed missing and duplicate values.
  - Ensured proper date format.
- Calculated new business metrics:
  - `Revenue = Quantity * Unit Price`
  - `Profit = Revenue - (Unit Cost * Quantity)`
- Filtered and aggregated data by:
  - Region
  - Product
  - Seller
  - Time period (month/year)

### 📥 **Load**
- Cleaned data exported to a new Excel file.
- Grouped outputs used for plots and dashboarding.

---

## 📊 Analysis and Visualizations

Visual insights were generated using `Matplotlib`, including:

- 📦 **Total Revenue by Product**
- 📍 **Revenue Trends by Month**
- 👨‍💼 **Top Sellers by Profit**

Example:

```python
df.groupby('Product')['Revenue'].sum().plot(kind='bar')
```




LinkedIn | GitHub
<div align="center"> <h2>👨‍💻 Author</h2>
<p>Mateus Barros</p>
<p>Data Engineering Intern</p> 
<a href="mailto:mateusbarrosds13@gmail.com"><img src="https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a> <a href="https://www.linkedin.com/in/mateus-barros13"><img src="https://img.shields.io/badge/-LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</div>
