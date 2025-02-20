import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the quadratic function to fit
def quadratic_function(time, a, b, c):
    return a * time**2 + b * time + c

# Generate time values (0 to 5 seconds)
time = np.linspace(0, 5, 100)

# Calculate corresponding height values (quadratic relationship)
height = 10 - 4.9 * time**2

# Add noise to simulate real data
np.random.seed(0)
noise = np.random.normal(0, 0.5, time.shape)
height_with_noise = height + noise

# Fit the quadratic function to the noisy data
params, covariance = curve_fit(quadratic_function, time, height_with_noise)

# Get the optimized parameters
a, b, c = params

# Create the fitted curve
fitted_curve = quadratic_function(time, a, b, c)

# Plot the noisy data and the fitted curve
plt.figure(figsize=(8, 6))
plt.scatter(time, height_with_noise, label='Noisy Data', color='blue')
plt.plot(time, fitted_curve, label='Fitted Curve', color='red')

# Add labels and title
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Projectile Motion of an Object')

# Print out parameters
print(f'a : {a}')
print(f'b : {b}')
print(f'c : {c}')

# Show legend and grid
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
