
import numpy as np

# Marks of 32 students in 4 subjects
student_scores = np.array([
    [85, 90, 78, 88],
    [92, 85, 80, 75],
    [78, 95, 88, 82],
    [90, 88, 92, 80],
    [76, 82, 85, 79],
    [88, 91, 84, 86],
    [95, 89, 90, 85],
    [80, 78, 82, 88],
    [84, 92, 86, 81],
    [91, 87, 89, 90],
    [73, 80, 78, 75],
    [89, 94, 91, 87],
    [82, 85, 83, 80],
    [94, 96, 88, 92],
    [77, 81, 79, 84],
    [86, 90, 92, 85],
    [90, 88, 85, 89],
    [81, 84, 87, 78],
    [93, 91, 94, 90],
    [79, 83, 80, 82],
    [88, 95, 89, 86],
    [85, 87, 91, 84],
    [92, 90, 86, 88],
    [74, 79, 82, 76],
    [87, 93, 90, 85],
    [83, 86, 84, 81],
    [96, 92, 95, 91],
    [80, 85, 88, 83],
    [89, 91, 87, 90],
    [78, 82, 85, 79],
    [91, 94, 92, 88],
    [84, 89, 86, 82]
])

# Subject names
subjects = ["Math", "Science", "English", "History"]

# Calculate average marks for each subject
average_scores = np.mean(student_scores, axis=0)

# Display average scores
for i in range(4):
    print(subjects[i], "Average:", round(average_scores[i], 2))

# Find the subject with the highest average
highest_index = np.argmax(average_scores)

print("Subject with highest average:", subjects[highest_index])
print("Highest average score:", round(average_scores[highest_index], 2))
