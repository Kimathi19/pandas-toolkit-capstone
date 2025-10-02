import pandas as pd

# Step 1: Read the messy CSV
print("📂 Reading messy sales data...")
df = pd.read_csv('data/messy_sales_data.csv')

# Step 2: Display first few rows
print("\n👀 First 5 rows of data:")
print(df.head())

# Step 3: Check the shape (rows, columns)
print(f"\n📊 Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")

# Step 4: Get detailed information about the dataset
print("\n📋 Dataset Information:")
print(df.info())

# Step 5: Check for missing values
print("\n❌ Missing Values Count (BEFORE cleaning):")
print(df.isnull().sum())

# Step 6: Basic statistics for numeric columns
print("\n📈 Basic Statistics:")
print(df.describe())

print("\n" + "="*50)
print("🧹 STARTING DATA CLEANING...")
print("="*50)

# Step 7: Fill missing Discounts with 0 (no discount)
print("\n1️⃣ Filling missing Discount values with 0...")
df['Discount'] = df['Discount'].fillna(0)

# Step 8: Drop rows with missing critical values
print("2️⃣ Dropping rows with missing Order_ID, Date, Quantity, or Unit_Price...")
initial_rows = len(df)
df = df.dropna(subset=['Order_ID', 'Date', 'Quantity', 'Unit_Price'])
dropped_rows = initial_rows - len(df)
print(f"   Dropped {dropped_rows} rows")

# Step 9: Check missing values after cleaning
print("\n✅ Missing Values Count (AFTER cleaning):")
print(df.isnull().sum())

print(f"\n📊 New dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")

# Step 10: Remove duplicate rows
print("\n3️⃣ Removing duplicate rows...")
initial_rows = len(df)
df = df.drop_duplicates()
dropped_duplicates = initial_rows - len(df)
print(f"   Removed {dropped_duplicates} duplicate rows")

# Step 11: Standardize Region names (convert to title case)
print("\n4️⃣ Standardizing Region names...")
print(f"   Before: {df['Region'].unique()}")
df['Region'] = df['Region'].str.strip().str.title()
print(f"   After: {df['Region'].unique()}")

# Step 12: Standardize Sales_Rep names (convert to title case)
print("\n5️⃣ Standardizing Sales_Rep names...")
print(f"   Before: {df['Sales_Rep'].unique()}")
df['Sales_Rep'] = df['Sales_Rep'].str.strip().str.title()
print(f"   After: {df['Sales_Rep'].unique()}")

print(f"\n📊 Dataset shape after removing duplicates: {df.shape[0]} rows, {df.shape[1]} columns")

# Step 13: Convert Date column to datetime
print("\n6️⃣ Converting Date to datetime format...")
print(f"   Before: Data type = {df['Date'].dtype}")
df['Date'] = pd.to_datetime(df['Date'])
print(f"   After: Data type = {df['Date'].dtype}")

# Step 14: Handle invalid emails
print("\n7️⃣ Cleaning invalid email addresses...")
print(f"   Invalid emails found: {(df['Customer_Email'] == 'INVALID').sum()}")
df['Customer_Email'] = df['Customer_Email'].replace('INVALID', 'unknown@email.com')
print(f"   Replaced with placeholder: 'unknown@email.com'")

print("\n" + "="*50)
print("📊 DATA ANALYSIS")
print("="*50)

# Step 15: Calculate Total Sales
print("\n💰 Calculating Total Sales...")
df['Total_Sales'] = df['Quantity'] * df['Unit_Price'] * (1 - df['Discount'])
print(f"   Total Sales column created!")
print(f"   Sample Total Sales values:\n{df[['Quantity', 'Unit_Price', 'Discount', 'Total_Sales']].head()}")

# Step 16: Overall business metrics
print(f"\n📈 Overall Business Metrics:")
print(f"   Total Revenue: ${df['Total_Sales'].sum():,.2f}")
print(f"   Average Order Value: ${df['Total_Sales'].mean():,.2f}")
print(f"   Total Orders: {len(df)}")

# Step 17: Sales by Region
print("\n🌍 Sales by Region:")
sales_by_region = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print(sales_by_region)
print(f"\n   Top Region: {sales_by_region.idxmax()} with ${sales_by_region.max():,.2f}")

# Step 18: Sales by Product
print("\n📦 Sales by Product:")
sales_by_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
print(sales_by_product)
print(f"\n   Top Product: {sales_by_product.idxmax()} with ${sales_by_product.max():,.2f}")

# Step 19: Average order value by Sales Rep
print("\n👤 Performance by Sales Rep:")
sales_rep_performance = df.groupby('Sales_Rep').agg({
    'Total_Sales': ['sum', 'mean', 'count']
}).round(2)
print(sales_rep_performance)

# Step 20: Extract time components
print("\n📅 Extracting time components...")
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.month_name()
df['Quarter'] = df['Date'].dt.quarter

# Step 21: Monthly sales trend
print("\n📈 Monthly Sales Trend:")
monthly_sales = df.groupby('Month_Name')['Total_Sales'].sum().sort_values(ascending=False)
print(monthly_sales)
print(f"\n   Best Month: {monthly_sales.idxmax()} with ${monthly_sales.max():,.2f}")

# Step 22: Quarterly sales
print("\n📊 Quarterly Sales:")
quarterly_sales = df.groupby('Quarter')['Total_Sales'].sum()
print(quarterly_sales)

# Step 23: Sales trend over time (by month number for chronological order)
print("\n📉 Chronological Monthly Trend:")
monthly_trend = df.groupby('Month')['Total_Sales'].sum()
print(monthly_trend)

print("\n" + "="*50)
print("💾 EXPORTING CLEAN DATA")
print("="*50)

# Step 24: Export cleaned data
print("\n📤 Exporting cleaned dataset...")
df.to_csv('output/clean_sales_data.csv', index=False)
print("   ✅ Saved to: output/clean_sales_data.csv")

# Step 25: Export summary statistics
print("\n📤 Exporting sales summary by region...")
sales_by_region.to_csv('output/sales_by_region.csv')
print("   ✅ Saved to: output/sales_by_region.csv")

print("\n📤 Exporting sales summary by product...")
sales_by_product.to_csv('output/sales_by_product.csv')
print("   ✅ Saved to: output/sales_by_product.csv")

print("\n" + "="*50)
print("✅ DATA CLEANING & ANALYSIS COMPLETE!")
print("="*50)
print(f"\n📊 Final Summary:")
print(f"   Original rows: 210")
print(f"   Final rows: {len(df)}")
print(f"   Columns: {len(df.columns)}")
print(f"   Total Revenue: ${df['Total_Sales'].sum():,.2f}")
print(f"   Files exported to 'output/' folder")