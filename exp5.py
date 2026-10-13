
import numpy as np

# Fuel efficiency of car models in miles per gallon (MPG)
fuel_efficiency = np.array([25, 30, 35, 40, 45])

# Display fuel efficiency data
print("Fuel Efficiency Data:")
print("Car Model A:", fuel_efficiency[0], "MPG")
print("Car Model B:", fuel_efficiency[1], "MPG")
print("Car Model C:", fuel_efficiency[2], "MPG")
print("Car Model D:", fuel_efficiency[3], "MPG")
print("Car Model E:", fuel_efficiency[4], "MPG")

# Calculate average fuel efficiency
average = np.mean(fuel_efficiency)

# Compare Car Model A and Car Model E
car1 = fuel_efficiency[0]
car2 = fuel_efficiency[4]

# Calculate percentage improvement
improvement = ((car2 - car1) / car1) * 100

# Display results
print("\nAverage Fuel Efficiency:", average, "MPG")
print("Car Model A Efficiency:", car1, "MPG")
print("Car Model E Efficiency:", car2, "MPG")
print("Percentage Improvement:", improvement, "%")
