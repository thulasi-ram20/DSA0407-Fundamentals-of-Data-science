import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Retail customer data
data = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Amount_Spent': [1000, 1500, 2000, 5000, 5500, 6000, 9000, 9500],
    'Visit_Frequency': [2, 3, 4, 6, 7, 8, 10, 12]
}

df = pd.DataFrame(data)

# Features
X = df[['Amount_Spent', 'Visit_Frequency']]

# K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = model.fit_predict(X)

print("Customer Segments:")
print(df)

# Plot clusters
plt.scatter(df['Amount_Spent'], df['Visit_Frequency'],
            c=df['Cluster'], cmap='viridis')

plt.xlabel("Amount Spent")
plt.ylabel("Visit Frequency")
plt.title("Retail Customer Segmentation")
plt.show()
