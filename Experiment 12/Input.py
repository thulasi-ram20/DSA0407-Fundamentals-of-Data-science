import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 150, 120, 180, 200, 250]

plt.scatter(months, sales)
plt.title("Monthly Sales Scatter Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
