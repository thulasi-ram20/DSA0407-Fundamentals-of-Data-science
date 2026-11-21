
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Control group
control = [10.9, 4.0, 6.0, 8.3, 6.9, 5.6, 11.6, 3.3,
           7.2, 2.9, 5.1, 5.2, 6.1, 3.8, 0.8, 5.1,
           6.2, 6.1, 5.5, 0.4]

# Treatment group
treatment = [10.3, 7.8, 12.8, 4.8, 10.1, 11.1, 11.1,
             5.9, 7.5, 13.4, 11.7, 11.4, 11.9, 10.0,
             8.4, 7.8, 12.4, 10.3, 11.5, 6.0]

# Calculate mean
print("Control Mean:", np.mean(control))
print("Treatment Mean:", np.mean(treatment))

# Hypothesis test
t_stat, p_value = ttest_ind(
    treatment, control, equal_var=False
)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Decision
if p_value < 0.05:
    print("Reject Null Hypothesis")
    print("Treatment has a significant effect")
else:
    print("Accept Null Hypothesis")
    print("No significant effect")

# Visualization
plt.boxplot([control, treatment],
            labels=["Control", "Treatment"])

plt.title("Treatment vs Placebo")
plt.ylabel("Symptom Improvement")
plt.show()
