# 🐼 Pandas Data Cleaning & Analysis Toolkit
## Prompt-Powered Kickstart: Building a Beginner's Guide to Pandas

**Author:** Brian Muriiki Kimathi  



## 🎯 Overview

This project demonstrates how to use **Pandas**, Python's most powerful data manipulation library, to clean and analyze messy real-world data. I used generative AI (Claude) to learn Pandas from scratch and built a complete data pipeline that:

- Reads messy CSV data with quality issues
- Cleans missing values, duplicates, and inconsistent formatting
- Performs data analysis and extracts business insights
- Exports clean data for further use

**End Goal:** Transform messy sales data into clean, analyzed insights ready for business decisions.

---

## Why Pandas?

I chose Pandas because:

1. **Foundation for Data Careers** - Essential for data engineering, data science, and analytics roles
2. **Industry Standard** - Used by companies worldwide for data manipulation
3. **Powerful & Versatile** - Handles everything from small CSVs to large datasets
4. **Career Alignment** - I'm transitioning from software engineering to data engineering, and Pandas is the core skill

**Real-World Use Cases:**
- Data cleaning and preprocessing
- ETL (Extract, Transform, Load) pipelines
- Business analytics and reporting
- Machine learning data preparation

---

## 📚 Technology Summary

### What is Pandas?

Pandas is a Python library for data manipulation and analysis. It provides:
- **DataFrames** - 2D tables (like Excel spreadsheets) that you can manipulate with code
- **Series** - 1D arrays (single columns of data)
- Powerful functions for reading, cleaning, transforming, and analyzing data

### Key Concepts:
- **DataFrame** - Main data structure (rows and columns)
- **Indexing** - Selecting specific rows/columns
- **GroupBy** - Aggregating data by categories
- **Missing Values** - Handling nulls/NaNs
- **Data Types** - Converting between text, numbers, dates

### Where is it Used?
- Data science and machine learning workflows
- Business intelligence and reporting
- Financial analysis
- Scientific research
- Web scraping and data collection

---

## 💻 System Requirements

- **OS:** Windows, macOS, or Linux
- **Python:** 3.7 or higher
- **Editor:** VS Code (recommended) or any text editor
- **Terminal/Command Line:** For running scripts

---

## 🔧 Installation & Setup

### Step 1: Check Python Installation
```bash
python --version
# or
python3 --version
```

You should see Python 3.7+ installed.

### Step 2: Install Required Libraries
```bash
pip install pandas numpy matplotlib
```

**What this installs:**
- `pandas` - Data manipulation
- `numpy` - Numerical operations (Pandas dependency)
- `matplotlib` - Basic plotting (optional, for future visualization)

### Step 3: Clone or Download This Repository
```bash
git clone [your-repo-url]
cd pandas-toolkit-capstone
```

### Step 4: Verify Project Structure
```
pandas-toolkit-capstone/
├── data/
│   └── messy_sales_data.csv
├── output/
│   ├── clean_sales_data.csv
│   ├── sales_by_region.csv
│   └── sales_by_product.csv
├── generate_messy_data.py
├── clean_and_analyze.py
└── README.md
```

---

## 🚀 Minimal Working Example

### Generate Messy Data (if needed)
```bash
python generate_messy_data.py
```

This creates `data/messy_sales_data.csv` with intentional data quality issues:
- Missing values in multiple columns
- Duplicate rows
- Inconsistent capitalization
- Invalid email addresses

### Run the Complete Data Pipeline
```bash
python clean_and_analyze.py
```

**What This Does:**
1. Reads the messy CSV file
2. Explores the data (shape, types, missing values)
3. Cleans missing values (fills discounts with 0, drops critical nulls)
4. Removes duplicate rows
5. Standardizes text (Region and Sales_Rep capitalization)
6. Converts Date column to datetime format
7. Fixes invalid emails
8. Calculates Total Sales per transaction
9. Analyzes sales by Region, Product, Sales Rep
10. Analyzes monthly and quarterly trends
11. Exports clean data and summaries to `output/` folder

### Expected Output
```
Reading messy sales data...
First 5 rows of data:
[Data preview]

Dataset shape: 210 rows, 9 columns
Missing Values Count (BEFORE cleaning):
[Missing value counts]

STARTING DATA CLEANING...
Missing Values Count (AFTER cleaning):
[Clean data confirmation]

DATA ANALYSIS
Total Revenue: $427,473.64
Top Region: East with $140,435.97
Top Product: Webcam with $106,359.99
Best Month: September

EXPORTING CLEAN DATA
Saved to: output/clean_sales_data.csv
```

---

## 🤖 AI Prompt Journal

Throughout this project, I used Claude (AI assistant) to learn Pandas. Here are the key prompts and what I learned:

### Prompt 1: Reading CSV Files
**Prompt Used:**  
*"How do I read a CSV file using Pandas in Python? Show me the basic code and explain what each part does."*

**AI Response Summary:**  
Claude explained `pd.read_csv()`, DataFrame concept, and `.head()` method for previewing data.

**My Evaluation:**  
Very helpful! Clear explanation with code examples. I learned that DataFrames are like Excel tables in Python.

**Code Learned:**
```python
import pandas as pd
df = pd.read_csv('data/messy_sales_data.csv')
print(df.head())
```

---

### Prompt 2: Exploring Data
**Prompt Used:**  
*"How can I get more information about my dataset in Pandas? I want to see data types, missing values, and basic statistics."*

**AI Response Summary:**  
Claude introduced `.info()`, `.describe()`, and `.isnull().sum()` methods for data profiling.

**My Evaluation:**  
 Essential for understanding data quality issues. Helped me identify which columns had problems.

**Code Learned:**
```python
df.info()  # Data types and non-null counts
df.isnull().sum()  # Missing value counts
df.describe()  # Statistical summary
```

---

### Prompt 3: Handling Missing Values
**Prompt Used:**  
*"What are the best practices for handling missing values in Pandas? Should I drop them, fill them, or something else?"*

**AI Response Summary:**  
Claude explained three strategies: dropping with `.dropna()`, filling with `.fillna()`, and keeping them. Context matters - critical columns should be dropped, optional columns can be filled.

**My Evaluation:**  
This was crucial! I learned that missing values require different strategies depending on what the column represents.

**Code Learned:**
```python
df['Discount'] = df['Discount'].fillna(0)  # Fill with 0
df = df.dropna(subset=['Order_ID', 'Date'])  # Drop critical nulls
```

---

### Prompt 4: Removing Duplicates & Text Standardization
**Prompt Used:**  
*"How do I remove duplicate rows in Pandas? And how can I standardize text data that has inconsistent capitalization?"*

**AI Response Summary:**  
Claude showed `.drop_duplicates()` for removing exact duplicate rows and `.str.title()`, `.str.lower()`, `.str.upper()` for standardizing text.

**My Evaluation:**  
Perfect timing! My data had "NORTH", "north", "North" all meaning the same thing.

**Code Learned:**
```python
df = df.drop_duplicates()
df['Region'] = df['Region'].str.strip().str.title()
```

---

### Prompt 5: Date Conversion
**Prompt Used:**  
*"How do I convert a text column to datetime format in Pandas? And why is this important for date analysis?"*

**AI Response Summary:**  
Claude explained `pd.to_datetime()` and why datetime format enables time-based analysis (extracting months, filtering date ranges, proper sorting).

**My Evaluation:**  
 Eye-opening! I didn't realize text dates can't be analyzed properly.

**Code Learned:**
```python
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
```

---

### Prompt 6: Creating Calculated Columns
**Prompt Used:**  
*"How do I create new calculated columns in Pandas? I want to calculate total sales from quantity, price, and discount columns."*

**AI Response Summary:**  
Claude showed how to create new columns by assigning calculations to a new column name.

**My Evaluation:**  
Simple but powerful! This is how you derive business metrics.

**Code Learned:**
```python
df['Total_Sales'] = df['Quantity'] * df['Unit_Price'] * (1 - df['Discount'])
```

---

### Prompt 7: Grouping Data
**Prompt Used:**  
*"How do I group data by categories in Pandas and calculate aggregated statistics? I want to see total sales by region and by product."*

**AI Response Summary:**  
Claude explained `.groupby()` for splitting data by categories and aggregating with `.sum()`, `.mean()`, `.count()`, etc.

**My Evaluation:**  
This is where Pandas really shines! GroupBy is incredibly powerful for analysis.

**Code Learned:**
```python
sales_by_region = df.groupby('Region')['Total_Sales'].sum()
sales_by_product = df.groupby('Product')['Total_Sales'].sum()
```

---

### Prompt 8: Time-Based Analysis
**Prompt Used:**  
*"How do I analyze time-based trends in Pandas? I want to see monthly sales patterns from my datetime column."*

**AI Response Summary:**  
Claude showed how to extract time components with `.dt.month`, `.dt.month_name()`, `.dt.quarter()` and group by them.

**My Evaluation:**  
Perfect for finding seasonal trends and patterns!

**Code Learned:**
```python
df['Month_Name'] = df['Date'].dt.month_name()
monthly_sales = df.groupby('Month_Name')['Total_Sales'].sum()
```

---

### Prompt 9: Exporting Data
**Prompt Used:**  
*"How do I export a Pandas DataFrame to a CSV file? I want to save my cleaned data."*

**AI Response Summary:**  
Claude explained `.to_csv()` with `index=False` to avoid exporting row numbers.

**My Evaluation:**  
Essential for sharing results and creating deliverables!

**Code Learned:**
```python
df.to_csv('output/clean_sales_data.csv', index=False)
```

---

## 📊 Results & Insights

### Data Quality Improvements
- **Original Dataset:** 210 rows
- **Rows Dropped:** 33 (missing critical values)
- **Duplicates Removed:** 10
- **Final Clean Dataset:** 167 rows
- **Missing Values:** 0 (all handled)

### Business Insights

**Overall Performance:**
- **Total Revenue:** $427,473.64
- **Average Order Value:** $2,559.72
- **Total Orders:** 167

**Regional Performance:**
- **Top Region:** East ($140,435.97)
- All regions standardized to title case (North, South, East, West)

**Product Performance:**
- **Top Product:** Webcam ($106,359.99)
- Product mix includes: Laptop, Mouse, Keyboard, Monitor, Headphones, Webcam, USB Cable

**Sales Rep Performance:**
- **Top Performer:** John Doe
- All names standardized to title case

**Temporal Trends:**
- **Best Quarter:** Q3
- **Best Month:** September
- Sales distributed across 2024

### Files Exported
1. `clean_sales_data.csv` - Complete cleaned dataset
2. `sales_by_region.csv` - Regional sales summary
3. `sales_by_product.csv` - Product sales summary

---

## ⚠️ Common Issues & Fixes

### Issue 1: ModuleNotFoundError: No module named 'pandas'
**Error:**
```
ModuleNotFoundError: No module named 'pandas'
```

**Solution:**
```bash
pip install pandas
# or if you have multiple Python versions:
pip3 install pandas
```

---

### Issue 2: FileNotFoundError when reading CSV
**Error:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/messy_sales_data.csv'
```

**Solution:**
- Ensure you're in the correct directory: `cd pandas-toolkit-capstone`
- Generate the data first: `python generate_messy_data.py`
- Check if `data/` folder exists: `ls` or `dir`

---

### Issue 3: SettingWithCopyWarning
**Warning:**
```
SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
```

**Solution:**
Use `.copy()` when creating subsets:
```python
df_subset = df[df['Region'] == 'North'].copy()
```

---

### Issue 4: Date not parsing correctly
**Error:**
```
ParserError: Unable to parse string at position 0
```

**Solution:**
Specify date format explicitly:
```python
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
```

---

### Issue 5: KeyError when accessing column
**Error:**
```
KeyError: 'Total_Sales'
```

**Solution:**
- Check column names: `print(df.columns)`
- Ensure you've created the column before accessing it
- Check for typos and case sensitivity

---

## 💡 What I Learned

### Technical Skills
1. **Data Profiling** - Understanding data before cleaning it
2. **Missing Value Strategies** - When to drop vs. fill
3. **Text Standardization** - Handling inconsistent data entry
4. **Data Type Conversion** - Especially datetime handling
5. **Calculated Columns** - Deriving business metrics
6. **GroupBy Operations** - Powerful aggregation techniques
7. **Time Series Basics** - Extracting temporal patterns

### AI-Assisted Learning
1. **Prompt Engineering** - How to ask clear, specific questions
2. **Iterative Learning** - Building knowledge step-by-step
3. **Documentation Habits** - Recording prompts and responses
4. **Problem Solving** - Using AI to debug and understand errors
5. **Efficiency** - Learning new technology in 4 days with AI assistance

### Data Engineering Mindset
1. **Data Quality Matters** - Garbage in, garbage out
2. **Document Everything** - Future you will thank present you
3. **Validate Results** - Check if numbers make sense
4. **Think About Users** - Clean data helps downstream consumers
5. **Automate Repetition** - Scripts beat manual work

---

## 📚 References

### Official Documentation
- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)

### Tutorials & Guides
- [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Real Python - Pandas DataFrames](https://realpython.com/pandas-dataframe/)

### Video Resources
- [Corey Schafer - Pandas Tutorial Series](https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)
- [Data School - Pandas Q&A](https://www.youtube.com/watch?v=yzIMircGU5I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y)

### Community Resources
- [Stack Overflow - Pandas Tag](https://stackoverflow.com/questions/tagged/pandas)
- [Kaggle Learn - Pandas](https://www.kaggle.com/learn/pandas)
- [DataCamp - Pandas Cheat Sheet](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python)

---

## 🚀 Next Steps

After completing this project, here are recommended next steps:

1. **Add Visualizations** - Use Matplotlib/Seaborn to create charts
2. **Learn SQL** - Combine Pandas with database queries
3. **Try Larger Datasets** - Work with millions of rows
4. **Explore Advanced Pandas** - MultiIndex, pivot tables, merges
5. **Build a Dashboard** - Use Streamlit or Plotly Dash
6. **Learn Data Engineering Tools** - Apache Airflow, dbt, Spark

---

## 🙏 Acknowledgments

- **Moringa School & We Think Code** - For the AI course curriculum


---

## 📝 License

This project is for educational purposes as part of the Moringa AI Capstone Project.

---

**Built with 🐼 Pandas and 🤖 AI!**
## **Happy Coding 🐼!**