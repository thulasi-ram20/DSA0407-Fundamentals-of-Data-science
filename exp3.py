
import numpy as np

# House data: [bedrooms, square footage, sale price]
house_data = np.array([
    [3, 1200, 200000],
    [5, 1800, 350000],
    [4, 1500, 280000],
    [6, 2200, 450000],
    [5, 2000, 400000],
    [2, 1000, 150000]
])

# Select houses with more than 4 bedrooms
selected_houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price (3rd column)
average_price = np.mean(selected_houses[:, 2])

print("Average sale price:", average_price)
