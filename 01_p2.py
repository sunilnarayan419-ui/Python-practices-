# To sum 2 numbers 

try:
    num_1 = float(input(f"Enter your first number : ")) 
    num_2 = float(input(f"Enter your second number : ")) 

    total = num_1 + num_2 
    print(f"Sum of {num_1} and {num_2} is {total:.3f}")  

except ValueError:
    print(f"Please enter valid numbers.")
