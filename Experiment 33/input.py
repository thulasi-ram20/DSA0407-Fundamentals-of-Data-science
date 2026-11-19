import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Car dataset
data = {
    'Engine': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
    'Horsepower': [70, 85, 100, 120, 150, 170, 200, 250],
    'Mileage': [20, 18, 17, 15, 14, 13, 12, 10],
    'Price': [300000, 400000, 500000, 650000,
              800000, 950000, 1200000, 1500000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Engine', 'Horsepower', 'Mileage']]
y = df['Price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Predicted Car Prices:", y_pred)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Important factors
print("\nFeature Importance (Regression Coefficients):")

for feature, value in zip(X.columns, model.coef_):
    print(feature, ":", value)

# Graph
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Car Price Prediction")
plt.show()
