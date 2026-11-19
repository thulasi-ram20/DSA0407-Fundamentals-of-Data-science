import pandas as pd
import matplotlib.pyplot as plt

# Create soccer player dataset
data = {
    'Name': ['Ronaldo', 'Messi', 'Neymar', 'Mbappe',
             'Haaland', 'Salah', 'Kane', 'Benzema'],
    'Age': [39, 37, 32, 26, 24, 32, 31, 36],
    'Position': ['Forward', 'Forward', 'Forward', 'Forward',
                 'Forward', 'Forward', 'Forward', 'Forward'],
    'Goals': [850, 820, 450, 300, 250, 300, 350, 480],
    'Salary': [500000, 600000, 400000, 550000,
               450000, 350000, 300000, 400000]
}

# Store data in CSV file
df = pd.DataFrame(data)
df.to_csv('players.csv', index=False)

# Read CSV file
df = pd.read_csv('players.csv')

print("Soccer Player Dataset:")
print(df)

# Top 5 players by goals
print("\nTop 5 Players with Highest Goals:")
print(df.nlargest(5, 'Goals')[['Name', 'Goals']])

# Top 5 players by salary
print("\nTop 5 Players with Highest Salaries:")
print(df.nlargest(5, 'Salary')[['Name', 'Salary']])

# Calculate average age
average_age = df['Age'].mean()

print("\nAverage Age:", average_age)

# Players above average age
print("\nPlayers Above Average Age:")
print(df[df['Age'] > average_age]['Name'])

# Position distribution
position_count = df['Position'].value_counts()

print("\nPlayer Position Distribution:")
print(position_count)

# Bar chart
position_count.plot(kind='bar')

plt.xlabel("Player Position")
plt.ylabel("Number of Players")
plt.title("Distribution of Soccer Players by Position")
plt.show()
