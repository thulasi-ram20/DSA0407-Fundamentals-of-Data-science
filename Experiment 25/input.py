
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X, y)

# Get flower measurements
print("Enter Iris Flower Measurements")

sl = float(input("Sepal Length: "))
sw = float(input("Sepal Width: "))
pl = float(input("Petal Length: "))
pw = float(input("Petal Width: "))

# Predict species
flower = [[sl, sw, pl, pw]]
prediction = model.predict(flower)

# Display result
print("\nPredicted Flower Species:",
      iris.target_names[prediction[0]])
