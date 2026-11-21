
import numpy as np
from scipy.stats import t

# Drug group
drug = [7.6, 12.2, 11.7, 8.4, 14.0, 3.7, 8.6, 15.6,
        3.3, 13.7, 13.7, 17.8, 11.1, 17.6, 18.3,
        10.6, 11.3, 13.1, 6.7, 13.4, 8.3, 10.1,
        14.1, 6.4, 16.1]

# Placebo group
placebo = [4.7, 1.3, 4.4, 5.7, -1.1, -0.3, 4.9,
           7.7, 1.4, 5.3, -1.7, 1.1, 3.8, 11.3,
           5.9, 7.9, -1.2, 0.5, 11.5, 5.6, -0.4,
           3.2, 5.9, 0.5, 0.7]

def confidence_interval(data):
    n = len(data)
    mean = np.mean(data)
    sd = np.std(data, ddof=1)
    se = sd / np.sqrt(n)

    critical = t.ppf(0.975, n - 1)

    lower = mean - critical * se
    upper = mean + critical * se

    print("Mean:", round(mean, 3))
    print("95% Confidence Interval:",
          round(lower, 3), "to", round(upper, 3))

print("Drug Group")
confidence_interval(drug)

print("\nPlacebo Group")
confidence_interval(placebo)
