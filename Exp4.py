
import numpy as np

# Quarterly sales data
sales_data = np.array([10000, 12000, 15000, 20000])

# Display quarterly sales
print("Quarterly Sales Data:")
print("First Quarter (Q1):", sales_data[0])
print("Second Quarter (Q2):", sales_data[1])
print("Third Quarter (Q3):", sales_data[2])
print("Fourth Quarter (Q4):", sales_data[3])

# Calculate total yearly sales
total_sales = np.sum(sales_data)

# Calculate percentage increase from Q1 to Q4
q1_sales = sales_data[0]
q4_sales = sales_data[3]

percentage_increase = ((q4_sales - q1_sales) / q1_sales) * 100

# Display results
print("\nTotal Sales for the Year:", total_sales)
print("Percentage Increase from Q1 to Q4:",
      percentage_increase, "%")
