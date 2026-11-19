import pandas as pd

# Temperature dataset
data = {
    'Chennai': [30, 32, 35, 33, 31],
    'Delhi': [20, 25, 30, 35, 40],
    'Mumbai': [28, 29, 30, 31, 32],
    'Bangalore': [22, 24, 25, 23, 26]
}

df = pd.DataFrame(data)

print("Temperature Data:")
print(df)

# Calculate mean
print("\nMean Temperature:")
print(df.mean())

# Calculate standard deviation
print("\nStandard Deviation:")
print(df.std())

# Calculate temperature range
temp_range = df.max() - df.min()

print("\nTemperature Range:")
print(temp_range)

# Highest temperature range
print("\nHighest Temperature Range:",
      temp_range.idxmax())

# Most consistent city
print("Most Consistent City:",
      df.std().idxmin())
