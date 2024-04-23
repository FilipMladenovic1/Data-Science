# Q1: Write 2 python function to get the indices of the sorted elements of given lists and compare the speed.
# one is without numpy package and the other is with numpy. (raise a error message if the input is null or not numerical)

import numpy as np
import random
import timeit

# Function to get the indices of sorted elements of a list without using NumPy
def sorted_indices_without_numpy(lst, list_name):
    # Check if the list is not empty and contains only numerical values
    if not lst or not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("The input is either null or not numerical!")
    # Sort the list and return the indices
    return sorted(range(len(lst)), key=lambda i: lst[i])

# Function to get the indices of sorted elements of a list using NumPy
def sorted_indices_with_numpy(lst, list_name):
    # Check if the list is not empty and contains only numerical values
    if not lst or not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("The input is either null or not numerical!")
    # Sort with NumPy and return the indices
    return np.argsort(lst)

# Function to classify the console output and run the sorted indices functions
def run_sorted_indices(function, lst, list_name):
    try:
        # Call the function and print the sorted indices
        indices = function(lst, list_name)
        print(f"Indices of sorted elements ({list_name}):", indices)
    except ValueError as e:
        # Print an error message if an error occurs
        print(f"Error for {list_name}:", e)

# Create test lists
List1 = [23, 104, 5, 190, 8, 7, -3]
List2 = []
List3 = [random.randint(0, 1000000) for _ in range(1000000)]

# Print the indices of sorted elements for each list
print("Without NumPy:")
run_sorted_indices(sorted_indices_without_numpy, List1, "List1")
run_sorted_indices(sorted_indices_without_numpy, List2, "List2")
run_sorted_indices(sorted_indices_without_numpy, List3, "List3")

print("With NumPy:")
run_sorted_indices(sorted_indices_with_numpy, List1, "List1")
run_sorted_indices(sorted_indices_with_numpy, List2, "List2")
run_sorted_indices(sorted_indices_with_numpy, List3, "List3")

# Measure the computational time with and without NumPy
time_without_numpy = 0
time_with_numpy = 0

# Time measurement for List1
if List1:
    time_without_numpy += timeit.timeit(lambda: sorted_indices_without_numpy(List1, "List1"), number=1)
    time_with_numpy += timeit.timeit(lambda: sorted_indices_with_numpy(List1, "List1"), number=1)

# Time measurement for List2
if List2:
    time_without_numpy += timeit.timeit(lambda: sorted_indices_without_numpy(List2, "List2"), number=1)
    time_with_numpy += timeit.timeit(lambda: sorted_indices_with_numpy(List2, "List2"), number=1)

# Time measurement for List3
if List3:
    time_without_numpy += timeit.timeit(lambda: sorted_indices_without_numpy(List3, "List3"), number=1)
    time_with_numpy += timeit.timeit(lambda: sorted_indices_with_numpy(List3, "List3"), number=1)

# Print the summerized computational times
print("Total computational time without NumPy:", time_without_numpy)
print("Total computational time with NumPy:", time_with_numpy)