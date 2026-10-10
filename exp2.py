
import numpy as np

# Sales data for 3 products over 3 sales
sales_data = np.array([
    [100, 150, 200],
    [250, 300, 350],
    [400, 450, 500]
])

# Calculate the average price of all products
average_price = np.mean(sales_data)

print("Average price of all products:", average_price)
