import pandas as pd

# Create sample sales data
data = {
    'Product': ['Mobile', 'Laptop', 'Headphones', 'Tablet',
                'Mobile', 'Smartwatch', 'Laptop', 'Headphones',
                'Tablet', 'Mobile'],
    'Quantity': [25, 10, 40, 15, 30, 20, 12, 35, 18, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total quantity sold for each product
sales = df.groupby('Product')['Quantity'].sum()

# Sort in descending order and select top 5
top_5 = sales.sort_values(ascending=False).head(5)

# Display output
print("Top 5 Best-Selling Products:")
print(top_5)
