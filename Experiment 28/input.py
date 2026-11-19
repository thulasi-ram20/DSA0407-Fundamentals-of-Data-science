import numpy as np
from sklearn.cluster import KMeans

# Customer shopping data
X = np.array([
    [1000, 2],
    [1500, 3],
    [2000, 4],
    [5000, 10],
    [6000, 12],
    [7000, 15]
])

# Train K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X)

# User input
amount = float(input("Enter shopping amount: "))
visits = int(input("Enter number of visits: "))

# Predict segment
segment = model.predict([[amount, visits]])

print("Customer belongs to Segment:", segment[0])
