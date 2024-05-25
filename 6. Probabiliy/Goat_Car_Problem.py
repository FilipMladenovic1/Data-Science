# Write a python / R function to simulate the Goat-car door open problem (Monty Hall problem) 100 times.

import random

def monty_hall_simulation(total_simulations):
    outcomes = []

    for _ in range(total_simulations):
        # Randomly place the car behind one of the three doors
        car_position = random.randint(0, 2)
        
        # Contestant makes an initial choice
        initial_choice = random.randint(0, 2)
        
        # Host opens a door that is neither the car nor the contestant's initial choice
        remaining_doors = [door for door in range(3) if door != initial_choice and door != car_position]
        monty_opens = random.choice(remaining_doors)
        
        # Determine the door to switch to (the other remaining door)
        switch_choice = next(door for door in range(3) if door != initial_choice and door != monty_opens)
        
        # Record the outcome
        outcomes.append((switch_choice == car_position, initial_choice == car_position))

    return outcomes

def get_success_counts(outcomes, num_simulations):
    switch_wins = sum(1 for i in range(num_simulations) if outcomes[i][0])
    stay_wins = sum(1 for i in range(num_simulations) if outcomes[i][1])
    return switch_wins, stay_wins

# Run the simulation 100 times and store outcomes
total_simulations = 100
outcomes = monty_hall_simulation(total_simulations)

# Get user input for the number of simulations to consider
num_simulations = int(input("Enter the number of simulations to consider: "))

# Ensure the input does not exceed the total number of simulations performed
if num_simulations > total_simulations:
    print(f"Number of simulations to consider cannot exceed {total_simulations}. Setting to {total_simulations}.")
    num_simulations = total_simulations

change_wins, stay_wins = get_success_counts(outcomes, num_simulations)

print(f"Number of wins if changed (first {num_simulations} simulations): {change_wins}")
print(f"Number of wins if stayed (first {num_simulations} simulations): {stay_wins}")

# Write the conclusion and what do you think?
# Answere: After running the code several times, I can conclude, that the success rate of switching doors is overall roughly equivalent to 2/3,
# whereas the success rate of not switching doors is overall roughly equivalent to 1/3. Considering the Bayesian rule, this outcome seems very accurate to me.