import numpy as np
import matplotlib.pyplot as plt

# Given variables
num_years = 80
ticket_price = 5

# Function to simulate one year of ticket purchases and lottery drawing with a specific number of tickets per person
def year_simul(num_tickets_per_person):
    total_spent = 0
    won = False

    for _ in range(num_years):
        # Ticket purchases for the year
        total_spent += num_tickets_per_person * ticket_price * 365
        
        # Simulate lottery draw
        winning_numbers = set(np.random.choice(range(1, 52), size=6, replace=False))  # State's winning numbers
        chosen_numbers = set(np.random.choice(range(1, 52), size=6, replace=False))  # Randomly chosen numbers

        # Check if chosen numbers are a winning combination
        if winning_numbers == chosen_numbers:
            won = True
            break
        
    return won, total_spent

# Function to calculate the minimum number of tickets per person needed for a win probability above 0.5
def calculate_tickets_needed():
    epsilon = 1e-5  # Desired probability epsilon (0.00001)

    # Start with one ticket per person
    num_tickets_per_person = 1

    win_probabilities = []  # Store win probabilities for visualization

    while True:
        # Simulate using the current number of tickets per person
        wins, _ = year_simul(num_tickets_per_person)
        winning_probability = wins / num_years  # Probability of winning in one year

        # Append the current win probability for visualization
        win_probabilities.append(winning_probability)

        # Check if the probability is above the desired epsilon
        if winning_probability > (0.5 + epsilon):
            break

        # Increment the number of tickets per person and continue
        num_tickets_per_person += 1

    return num_tickets_per_person, win_probabilities

# Calculate the minimum number of tickets per person needed for a win probability above 0.5 and collect win probabilities
min_tickets_needed, win_probabilities = calculate_tickets_needed()

# Display the results
print(f"Minimum number of tickets per person for win probability > 0.5: {min_tickets_needed}")

# Visualize the relationship between the number of tickets per person and win probabilities
plt.figure(figsize=(10, 6))
plt.plot(range(1, min_tickets_needed + 1), win_probabilities)
plt.xlabel('Number of Tickets per Person')
plt.ylabel('Win Probability')
plt.title('Win Probability vs. Number of Tickets per Person')
plt.grid(True)
plt.show()

