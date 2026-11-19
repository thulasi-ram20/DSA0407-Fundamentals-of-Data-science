
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample dataset
X = np.array([
    [1000, 2],
    [1500, 3],
    [2000, 3],
    [2500, 4],
    [3000, 5],
    [1800, 3]
])

y = np.array([2000000, 3000000, 4000000,
              5000000, 6000000, 3600000])

# Train the model
model = LinearRegression()
model.fit(X, y)

# User input
area = float(input("Enter house area (sq.ft): "))
bedrooms = int(input("Enter number of bedrooms: "))

# Prediction
price = model.predict([[area, bedrooms]])

print("Predicted House Price: Rs.", round(price[0], 2))
