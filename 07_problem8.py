# to generate a list of random integers within a specified range. 

import random 

def generate_random_numbers(count, lower_bound, upper_bound):
    """Generate a list of random integers within a specified range.

    Args:
        count (int): The number of random integers to generate.
        lower_bound (int): The lower bound of the range (inclusive).
        upper_bound (int): The upper bound of the range (inclusive).

    Returns:
        list: A list containing the generated random integers.
    """
    random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(count)]
    return random_numbers   

try:
    count = int(input("Enter the number of random integers to generate: ").strip())
    lower_bound = int(input("Enter the lower bound (inclusive): ").strip())
    upper_bound = int(input("Enter the upper bound (inclusive): ").strip())

    if count <= 0 or lower_bound > upper_bound:
        raise ValueError("Invalid input values.")

    random_numbers = generate_random_numbers(count, lower_bound, upper_bound)
    print(f"Generated random numbers: {random_numbers}")   
except ValueError as e:
    print(f"Error: {e}")    