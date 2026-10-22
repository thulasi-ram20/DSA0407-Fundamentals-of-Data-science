import matplotlib.pyplot as plt

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [12000, 15000, 10000, 18000, 22000, 20000]

# 1. Line plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o')
plt.title('Monthly Sales - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# 2. Bar plot
plt.figure(figsize=(8, 5))
plt.bar(months, sales)
plt.title('Monthly Sales - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
