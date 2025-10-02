import csv
import random
from datetime import datetime, timedelta

# Generate messy sales data
data = []

# Product catalog
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'USB Cable']
regions = ['North', 'South', 'East', 'West', 'NORTH', 'south', 'east']  # Inconsistent capitalization
sales_reps = ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Williams', 'John Doe', 'jane smith']  # Duplicates & case issues

# Generate 200 rows of data
start_date = datetime(2024, 1, 1)

for i in range(200):
    date = start_date + timedelta(days=random.randint(0, 365))
    
    # Introduce various data quality issues
    row = {
        'Order_ID': f'ORD{str(i+1).zfill(3)}' if random.random() > 0.05 else '',  # 5% missing order IDs
        'Date': date.strftime('%Y-%m-%d') if random.random() > 0.03 else '',  # 3% missing dates
        'Product': random.choice(products),
        'Quantity': random.randint(1, 20) if random.random() > 0.07 else '',  # 7% missing quantities
        'Unit_Price': round(random.uniform(10, 500), 2) if random.random() > 0.04 else '',  # 4% missing prices
        'Region': random.choice(regions),  # Inconsistent capitalization
        'Sales_Rep': random.choice(sales_reps),  # Duplicate names with different cases
        'Customer_Email': f'customer{i}@email.com' if random.random() > 0.1 else 'INVALID',  # 10% invalid emails
        'Discount': round(random.uniform(0, 0.3), 2) if random.random() > 0.5 else '',  # 50% missing discounts
    }
    
    data.append(row)

# Add some duplicate rows (exact duplicates)
for _ in range(10):
    data.append(random.choice(data).copy())

# Shuffle the data
random.shuffle(data)

# Write to CSV
with open('data/messy_sales_data.csv', 'w', newline='') as f:
    fieldnames = ['Order_ID', 'Date', 'Product', 'Quantity', 'Unit_Price', 'Region', 'Sales_Rep', 'Customer_Email', 'Discount']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("✅ Messy sales data generated: data/messy_sales_data.csv")
print(f"📊 Total rows: {len(data)}")
print("\n🔴 Intentional data quality issues:")
print("  - Missing values in multiple columns")
print("  - Duplicate rows")
print("  - Inconsistent capitalization (regions, names)")
print("  - Invalid email addresses")
print("  - Missing discount values")