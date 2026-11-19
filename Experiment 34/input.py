import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Patient dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 28, 48],
    'Gender': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'BP': [110, 120, 130, 140, 150, 160, 145, 155, 115, 135],
    'Cholesterol': [180, 190, 200, 220, 230, 240, 210, 250, 185, 205],
    'Outcome': ['Good', 'Good', 'Good', 'Bad', 'Bad',
                'Bad', 'Bad', 'Bad', 'Good', 'Good']
}

df = pd.DataFrame(data)

X = df[['Age', 'Gender', 'BP', 'Cholesterol']]
y = df['Outcome']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print("Actual Outcomes:", list(y_test))
print("Predicted Outcomes:", list(y_pred))

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, pos_label='Good'))
print("Recall:", recall_score(y_test, y_pred, pos_label='Good'))
print("F1 Score:", f1_score(y_test, y_pred, pos_label='Good'))
