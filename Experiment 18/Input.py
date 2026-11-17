
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Given data
age = [23, 23, 27, 27, 39, 41, 47, 49, 50,
       52, 54, 54, 56, 57, 58, 58, 60, 61]

fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4,
       27.2, 31.2, 34.6, 42.5, 28.8, 33.4,
       30.2, 34.1, 32.9, 41.2, 35.7]

# Create DataFrame
df = pd.DataFrame({
    'Age': age,
    'Body Fat': fat
})

# Calculate statistics
print("Statistical Analysis")
print(df.agg(['mean', 'median', 'std']))

# Draw boxplots
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'])
plt.title("Boxplot of Age")

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Body Fat'])
plt.title("Boxplot of Body Fat")

plt.tight_layout()
plt.show()

# Draw scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(df['Age'], df['Body Fat'])
plt.xlabel("Age")
plt.ylabel("Body Fat Percentage")
plt.title("Age vs Body Fat")
plt.grid()
plt.show()

# Draw Q-Q plots
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")

plt.subplot(1, 2, 2)
stats.probplot(df['Body Fat'], dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat")

plt.tight_layout()
plt.show()
