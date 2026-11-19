
import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample dataset
X = np.array([
    [100, 1],
    [200, 2],
    [300, 3],
    [400, 4],
    [500, 5],
    [150, 1],
    [450, 4],
    [250, 2]
])

y = np.array([1, 1, 0, 0, 0, 1, 0, 1])

# Train the model
model = LogisticRegression()
model.fit(X, y)

# User input
minutes = float(input("Enter usage minutes: "))
duration = int(input("Enter contract duration (months): "))

# Prediction
result = model.predict([[minutes, duration]])

if result[0] == 1:
    print("Customer is likely to churn.")
else:
    print("Customer is not likely to churn.")
