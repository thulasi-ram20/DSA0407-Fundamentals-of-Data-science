
import pandas as pd
import numpy as np
from scipy import stats

# Read CSV file
data = pd.read_csv("customer_reviews.csv")

# Get customer ratings
ratings = data["Rating"].dropna()

# Calculate statistics
n = len(ratings)
mean = ratings.mean()
sd = ratings.std()

# Set confidence level
confidence = 0.95

# Calculate confidence interval
t_value = stats.t.ppf(0.975, n - 1)
margin = t_value * (sd / np.sqrt(n))

lower = mean - margin
upper = mean + margin

# Display results
print("Customer Rating Analysis")
print("Number of Reviews:", n)
print("Average Rating:", round(mean, 2))
print("Standard Deviation:", round(sd, 2))

print("95% Confidence Interval:",
      round(lower, 2), "to", round(upper, 2))

# Customer satisfaction
if mean >= 4:
    print("Customer Satisfaction: Highly Satisfied")
elif mean >= 3:
    print("Customer Satisfaction: Moderately Satisfied")
else:
    print("Customer Satisfaction: Low Satisfaction")
