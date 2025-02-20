import random
import matplotlib.pyplot as plt

def simulate_depreciation(initial_value, depreciation_rate, years):
    """
    Simulate car depreciation using a simple probabilistic model.

    Args:
    initial_value (float): The initial value of the car (in dollars).
    depreciation_rate (float): The annual depreciation rate (as a decimal).
    years (int): The number of years to simulate depreciation for.

    Returns:
    list: A list containing the car's value for each year.
    """
    car_value = initial_value
    car_values = []

    for year in range(1, years + 1):
        # Apply depreciation
        depreciation = car_value * depreciation_rate
        car_value -= depreciation
        car_values.append(car_value)

    return car_values


# Car information
initial_value = 25000
depreciation_rate = 0.15
years_to_simulate = 5

# Simulate car depreciation
car_values = simulate_depreciation(initial_value, depreciation_rate, years_to_simulate)

# Create a visualization
years = range(1, years_to_simulate + 1)
plt.plot(years, car_values, marker='o', linestyle='-', color='b')
plt.title('Car Depreciation Over Time')
plt.xlabel('Years')
plt.ylabel('Car Value ($)')
plt.grid(True)

# Show the plot
plt.show()
