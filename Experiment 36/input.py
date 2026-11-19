import pandas as pd
import matplotlib.pyplot as plt

# Create sample stock CSV file
data = {
    'Date': ['Day1', 'Day2', 'Day3', 'Day4', 'Day5',
             'Day6', 'Day7', 'Day8'],
    'Closing_Price': [100, 105, 102, 110, 108, 115, 112, 120]
}

df = pd.DataFrame(data)
df.to_csv('stock_data.csv', index=False)

# Read CSV file
df = pd.read_csv('stock_data.csv')

print("Stock Data:")
print(df)

# Calculate variability
mean = df['Closing_Price'].mean()
std = df['Closing_Price'].std()
variance = df['Closing_Price'].var()
price_range = df['Closing_Price'].max() - df['Closing_Price'].min()

print("\nMean Price:", mean)
print("Standard Deviation:", std)
print("Variance:", variance)
print("Price Range:", price_range)

# Plot stock prices
plt.plot(df['Date'], df['Closing_Price'], marker='o')

plt.xlabel("Trading Days")
plt.ylabel("Closing Price")
plt.title("Stock Price Variability")
plt.grid()
plt.show()
