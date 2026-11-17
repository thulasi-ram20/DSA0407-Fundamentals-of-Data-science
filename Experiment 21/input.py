
import numpy as np
import pandas as pd
from scipy import stats

# Read data from CSV file
data = pd.read_csv("rare_elements.csv")

# Get concentration values
values = data.iloc[:, 0].dropna().to_numpy()

# Get user inputs
n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (%): "))
precision = float(input("Enter desired precision: "))

# Validate inputs
if n <= 1 or n > len(values):
    print("Invalid sample size!")
elif confidence <= 0 or confidence >= 100 or precision <= 0:
    print("Invalid confidence level or precision!")
else:
    # Select random sample
    sample = np.random.choice(values, n, replace=False)

    # Calculate point estimate
    mean = np.mean(sample)
    sd = np.std(sample, ddof=1)

    # Calculate confidence interval
    alpha = 1 - confidence / 100
    t_value = stats.t.ppf(1 - alpha/2, n-1)

    margin = t_value * sd / np.sqrt(n)

    lower = mean - margin
    upper = mean + margin

    # Display results
    print("\nPoint Estimate:", round(mean, 3))
    print("Standard Deviation:", round(sd, 3))
    print("Confidence Interval:",
          round(lower, 3), "to", round(upper, 3))
    print("Margin of Error:", round(margin, 3))

    if margin <= precision:
        print("Desired precision achieved.")
    else:
        print("Desired precision not achieved.")
