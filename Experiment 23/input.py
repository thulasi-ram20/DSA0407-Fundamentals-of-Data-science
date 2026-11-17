
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Sample data
control = [45, 48, 50, 47, 46, 49, 51, 44, 48, 47]

treatment = [35, 38, 40, 36, 34, 39, 37, 35, 38, 36]

# Calculate mean
mean_control = np.mean(control)
mean_treatment = np.mean(treatment)

print("Control Group Mean:", mean_control)
print("Treatment Group Mean:", mean_treatment)

# Hypothesis testing
# H0: No significant difference
# H1: Significant difference

t_stat, p_value = stats.ttest_ind(
    control, treatment, equal_var=False
)

print("\nT-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 6))

# Check significance
if p_value < 0.05:
    print("Reject Null Hypothesis")
    print("Treatment has a significant effect.")
else:
    print("Accept Null Hypothesis")
    print("Treatment has no significant effect.")

# Visualization
groups = ['Control', 'Treatment']
means = [mean_control, mean_treatment]

plt.bar(groups, means)
plt.title("Comparison of Control and Treatment Groups")
plt.xlabel("Groups")
plt.ylabel("Mean Measurement")
plt.show()

# P-value visualization
plt.figure()
plt.bar(['P-value', 'Significance Level'],
        [p_value, 0.05])
plt.title("P-value Comparison")
plt.ylabel("Value")
plt.show()
