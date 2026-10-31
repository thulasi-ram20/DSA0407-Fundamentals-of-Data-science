import pandas as pd

data = {
    'Post': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
    'Likes': [100, 200, 100, 300, 200, 100]
}

df = pd.DataFrame(data)

frequency = df['Likes'].value_counts().sort_index()

print("Frequency Distribution of Likes:")
print(frequency)
