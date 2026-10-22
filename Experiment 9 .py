import pandas as pd

# Sample property data
data = {
    'property_id': [101, 102, 103, 104, 105, 106],
    'location': ['Chennai', 'Bangalore', 'Chennai', 'Hyderabad',
                 'Bangalore', 'Chennai'],
    'bedrooms': [3, 5, 4, 6, 2, 5],
    'area_sqft': [1200, 2500, 1800, 3000, 1000, 3500],
    'listing_price': [5000000, 8000000, 6500000, 9000000,
                      4000000, 10000000]
}

# Create DataFrame
property_data = pd.DataFrame(data)

# 1. Average listing price in each location
print("1. Average Listing Price in Each Location:")
print(property_data.groupby('location')['listing_price'].mean())

# 2. Number of properties with more than four bedrooms
print("\n2. Properties with More Than Four Bedrooms:")
print((property_data['bedrooms'] > 4).sum())

# 3. Property with the largest area
print("\n3. Property with the Largest Area:")
print(property_data.loc[property_data['area_sqft'].idxmax()])
