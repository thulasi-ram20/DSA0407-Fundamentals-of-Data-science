import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Transaction dataset
data = {
    'Customer_ID': [101, 101, 102, 102, 103, 103,
                    104, 104, 105, 105, 106, 106],
    'Amount': [500, 700, 1000, 1200, 2000, 1800,
               4000, 4500, 5000, 5500, 7000, 7500],
    'Items': [2, 3, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14]
}

df = pd.DataFrame(data)

# Group transactions by customer
customer_data = df.groupby('Customer_ID')[
    ['Amount', 'Items']
].sum().reset_index()

print("Customer Purchase Data:")
print(customer_data)

# Select features
X = customer_data[['Amount', 'Items']]

# Apply K-Means
model = KMeans(n_clusters=3, random_state=42, n_init=10)
customer_data['Cluster'] = model.fit_predict(X)

print("\nCustomer Clusters:")
print(customer_data)

# Visualize clusters
plt.scatter(
    customer_data['Amount'],
    customer_data['Items'],
    c=customer_data['Cluster'],
    cmap='rainbow'
)

plt.xlabel("Total Amount Spent")
plt.ylabel("Total Items Purchased")
plt.title("Customer Segmentation Using K-Means")
plt.show()
