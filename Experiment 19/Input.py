
import numpy as np
from scipy import stats

# Enter blood pressure reduction data
drug = [12, 15, 10, 14, 13, 16, 11, 15, 14, 12]
placebo = [5, 7, 4, 6, 8, 5, 6, 7, 4, 5]

# Function to calculate confidence interval
def confidence_interval(data):
    n = len(data)
    mean = np.mean(data)
    sd = np.std(data, ddof=1)

    margin = stats.t.ppf(0.975, n-1) * sd / np.sqrt(n)

    lower = mean - margin
    upper = mean + margin

    return mean, lower, upper

# Drug group
mean1, lower1, upper1 = confidence_interval(drug)

# Placebo group
mean2, lower2, upper2 = confidence_interval(placebo)

# Display results
print("NEW DRUG GROUP")
print("Mean reduction:", round(mean1, 2))
print("95% Confidence Interval:", round(lower1, 2),
      "to", round(upper1, 2))

print("\nPLACEBO GROUP")
print("Mean reduction:", round(mean2, 2))
print("95% Confidence Interval:", round(lower2, 2),
      "to", round(upper2, 2))
