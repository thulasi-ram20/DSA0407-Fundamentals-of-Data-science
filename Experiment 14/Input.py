import pandas as pd

data = {
    'Customer': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Age': [20, 25, 20, 30, 25, 20]
}

df = pd.DataFrame(data)

frequency = df['Age'].value_counts().sort_index()

print("Customer Age Frequency Distribution:")
print(frequency)
