import math
from math import comb
import matplotlib.pyplot as plt

def calculate_probability_of_winning():
    # Total number of possible combinations
    total_combinations = comb(51, 6)
    
    # Number of ways to win the consolation prize (3 out of 6 numbers)
    ways_to_win = comb(6, 3) * comb(45, 3)
    
    # Probability of winning the consolation prize
    probability = ways_to_win / total_combinations
    
    return probability

def calculate_expected_value(probability, prize_amount):
    # Expected value = Probability of winning * Prize amount
    expected_value = probability * prize_amount
    
    return expected_value

# Define the prize amount for the consolation prize
prize_amount = 1200000000  

# Calculate the probability of winning the consolation prize
probability = calculate_probability_of_winning()

# Calculate the expected value of the consolation prize
expected_value = calculate_expected_value(probability, prize_amount)

# Create a bar chart to visualize the prize amount and expected value
labels = ["Prize Amount", "Expected Value"]
values = [prize_amount, expected_value]
colors = ["blue", "green"]

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=colors)
plt.title("Prize Amount vs. Expected Value")
plt.ylabel("Amount ($)")
plt.grid(axis="y")
plt.show()

print(f"The probability of winning the consolation prize is approximately {probability:.10f}")
print(f"The expected value of the consolation prize is ${expected_value:.2f}")
# Determine if the consolation prize is likely to increase sales
if expected_value > 0:
    print("The consolation prize is likely to increase sales.")
else:
    print("The consolation prize may not significantly impact sales.")
