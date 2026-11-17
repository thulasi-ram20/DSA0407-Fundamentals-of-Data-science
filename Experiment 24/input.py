
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Sample patient dataset
X = np.array([
    [1, 2],
    [2, 3],
    [3, 3],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 9]
])

# Labels: 0 = No condition, 1 = Condition
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Get new patient details
print("Enter patient symptom details:")
fever = float(input("Enter fever level: "))
cough = float(input("Enter cough level: "))

k = int(input("Enter value of k: "))

# Validate k
if k < 1 or k > len(X):
    print("Invalid value of k!")
else:
    # Create KNN classifier
    model = KNeighborsClassifier(n_neighbors=k)

    # Train the model
    model.fit(X, y)

    # Predict condition
    patient = np.array([[fever, cough]])
    prediction = model.predict(patient)

    # Display result
    print("\nPrediction:")

    if prediction[0] == 1:
        print("Patient has the medical condition.")
    else:
        print("Patient does not have the medical condition.")
