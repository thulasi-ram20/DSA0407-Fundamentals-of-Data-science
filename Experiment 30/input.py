import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_text

# Car dataset
X = np.array([
    [20000, 2, 1000],
    [30000, 3, 1200],
    [40000, 4, 1500],
    [50000, 5, 1800],
    [60000, 6, 2000],
    [70000, 7, 2200]
])

y = np.array([800000, 700000, 600000,
              500000, 400000, 300000])

# Train CART model
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# User input
mileage = float(input("Enter car mileage: "))
age = float(input("Enter car age: "))
engine = float(input("Enter engine capacity: "))

# Prediction
prediction = model.predict([[mileage, age, engine]])

print("Predicted Car Price: Rs.", prediction[0])

# Display decision tree rules
print("\nDecision Path:")
print(export_text(model, feature_names=[
    "Mileage", "Age", "Engine"
]))

# Display conditions for new car
node_indicator = model.decision_path([[mileage, age, engine]])
leaf_id = model.apply([[mileage, age, engine]])[0]

print("Nodes followed:", node_indicator.indices)
print("Final prediction leaf:", leaf_id)
