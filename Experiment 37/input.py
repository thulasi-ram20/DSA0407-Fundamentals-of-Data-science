import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Student dataset
data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam_Scores': [35, 40, 50, 55, 60, 65, 75, 80, 90, 95]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Calculate correlation
correlation = df['Study_Hours'].corr(df['Exam_Scores'])

print("\nCorrelation:", correlation)

if correlation > 0:
    print("Positive Correlation")
elif correlation < 0:
    print("Negative Correlation")
else:
    print("No Correlation")

# Scatter plot
plt.scatter(df['Study_Hours'], df['Exam_Scores'])
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Time vs Exam Scores")
plt.show()

# Line plot
plt.plot(df['Study_Hours'], df['Exam_Scores'], marker='o')
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Hours and Exam Scores")
plt.show()

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
