import numpy as np
import matplotlib.pyplot as plt

def calculate_depreciation(initial_value, years, num_simulations):
    """
    Simulate car depreciation using a Monte Carlo simulation.

    Args:
    initial_value (float): The initial value of the car (in dollars).
    years (int): The number of years to simulate depreciation for.
    num_simulations (int): The number of simulation scenarios to run.

    Returns:
    np.array: An array containing the car's value for each simulation scenario and year.
    """
    depreciation_rates = np.random.normal(0.15, 0.03, size=(num_simulations, years))
    car_values = np.zeros((num_simulations, years))
    car_values[:, 0] = initial_value

    for year in range(1, years):
        car_values[:, year] = car_values[:, year - 1] * (1 - depreciation_rates[:, year])

    return car_values

# Car information
initial_value = 25000  # Initial value of the car in dollars
years_to_simulate = 5  # Number of years to simulate depreciation
num_simulations = 1000  # Number of Monte Carlo simulations

# Simulate car depreciation
car_values = calculate_depreciation(initial_value, years_to_simulate, num_simulations)

# Plot the results for a few scenarios
for i in range(5):
    plt.plot(range(years_to_simulate), car_values[i], label=f'Simulation {i+1}')

plt.xlabel('Years')
plt.ylabel('Car Value ($)')
plt.title('Car Depreciation (Monte Carlo Simulation)')
plt.legend()
plt.grid(True)
plt.show()