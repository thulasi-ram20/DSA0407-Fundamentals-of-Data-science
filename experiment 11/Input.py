import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 150, 120, 180, 200, 250]

plt.plot(months, sales, marker='o')
plt.title("Monthly Product Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
