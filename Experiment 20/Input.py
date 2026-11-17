
import numpy as np
from scipy import stats

# Conversion rate data (sample values)
design_A = [12, 14, 13, 15, 11, 14, 16, 13, 12, 15]

design_B = [18, 20, 17, 19, 21, 18, 22, 20, 19, 21]

# Calculate mean conversion rates
mean_A = np.mean(design_A)
mean_B = np.mean(design_B)

print("Mean Conversion Rate of Design A:", mean_A)
print("Mean Conversion Rate of Design B:", mean_B)

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(
    design_A, design_B, equal_var=False
)

print("\nT-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 4))

# Check statistical significance
if p_value < 0.05:
    print("There is a statistically significant difference.")
else:
    print("There is no statistically significant difference.")
