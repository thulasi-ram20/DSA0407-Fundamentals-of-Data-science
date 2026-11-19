import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Customer dataset
data = {
    'Age': [20, 25, 30, 35, 40, 45, 50, 55],
    'Spending': [1000, 1500, 2000, 5000, 5500, 6000, 9000, 9500],
    'Visits': [2, 3, 4, 6, 7, 8, 10, 12]
}

df = pd.DataFrame(data)

# Select features
X = df[['Age', 'Spending', 'Visits']]

# Apply K-Means
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Segment'] = model.fit_predict(X)

print("Customer Segments:")
print(df)

# Visualize clusters
plt.scatter(df['Age'], df['Spending'],
            c=df['Segment'], cmap='rainbow')

plt.xlabel("Age")
plt.ylabel("Spending")
plt.title("Customer Segmentation")
plt.show()
