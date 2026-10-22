import pandas as pd

# Create sample order data
data = {
    'customer_id': [101, 102, 101, 103, 102, 101],
    'order_date': ['2026-01-05', '2026-01-07', '2026-01-10',
                   '2026-01-12', '2026-01-15', '2026-01-20'],
    'product_name': ['Laptop', 'Mouse', 'Laptop',
                     'Keyboard', 'Mouse', 'Keyboard'],
    'order_quantity': [1, 2, 1, 3, 4, 2]
}

# Create DataFrame
order_data = pd.DataFrame(data)

# Convert order_date into datetime format
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# Display the original data
print("Order Data:")
print(order_data)

# 1. Total number of orders made by each customer
print("\n1. Total orders made by each customer:")
print(order_data.groupby('customer_id').size())

# 2. Average order quantity for each product
print("\n2. Average order quantity for each product:")
print(order_data.groupby('product_name')['order_quantity'].mean())

# 3. Earliest and latest order dates
print("\n3. Earliest and latest order dates:")
print("Earliest order date:", order_data['order_date'].min())
print("Latest order date:", order_data['order_date'].max())
