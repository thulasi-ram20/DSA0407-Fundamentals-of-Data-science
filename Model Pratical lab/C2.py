
import numpy as np

# Stock closing prices
prices = [150.2, 151.8, 149.5, 152.3, 154.1,
          153.6, 155.9, 157.2, 156.0, 158.4,
          160.1, 159.3, 157.8, 159.9, 162.5,
          161.2, 163.8, 165.0, 164.1, 166.7]

# Calculate statistics
variance = np.var(prices, ddof=1)
std_dev = np.std(prices, ddof=1)
price_range = max(prices) - min(prices)

# Display output
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(std_dev, 2))
print("Range:", round(price_range, 2))
