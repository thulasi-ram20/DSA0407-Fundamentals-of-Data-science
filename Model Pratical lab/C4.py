
import numpy as np
from scipy.stats import ttest_ind

# Conversion rates of Design A
A = [2.1, 2.4, 1.9, 2.6, 2.2,
     2.3, 2.0, 2.5, 2.2, 2.4]

# Conversion rates of Design B
B = [2.8, 3.1, 2.7, 3.0, 2.9,
     3.3, 2.6, 3.2, 2.9, 3.0]

# Calculate means
print("Mean of Design A:", np.mean(A))
print("Mean of Design B:", np.mean(B))

# Perform independent t-test
t_stat, p_value = ttest_ind(
    A, B, equal_var=False
)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Hypothesis testing
if p_value < 0.05:
    print("Reject Null Hypothesis")
    print("Significant difference exists")
else:
    print("Accept Null Hypothesis")
    print("No significant difference")
