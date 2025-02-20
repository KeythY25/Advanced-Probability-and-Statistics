# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset for Crime Rates and Police Presence
np.random.seed(0)  
# Random crime rates between 50 and 500
crime_rates = np.random.uniform(50, 500, 100)  
# Randomized police presence 
police_presence = 1000 - 2 * crime_rates + np.random.normal(0, 100, 100)

# Calculate the correlation coefficient
correlation_coefficient = np.corrcoef(crime_rates, police_presence)[0, 1]

# Print the correlation coefficient
print("Correlation coefficient between Crime Rates and Police Presence:", correlation_coefficient)

# Perform linear regression
slope, intercept = np.polyfit(crime_rates, police_presence, 1)
regression_line = slope * np.array(crime_rates) + intercept

# Create a scatter plot with the regression line
plt.scatter(crime_rates, police_presence, label="Data Points")
plt.plot(crime_rates, regression_line, color='red', label="Linear Regression Line")
plt.title("Correlation Between Crime Rates and Police Presence with Linear Regression")
plt.xlabel("Crime Rates")
plt.ylabel("Police Presence")
plt.legend()

# Show the plot
plt.show()
