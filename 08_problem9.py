# this program computes the factorial of a given positive integer n
# and displays the factorial sequence in a graphical form

import matplotlib.pyplot as plt  

def  factorial(n):
    """returns the factorial in sequence""" 
    sequence = []
    result = 1 
    for i in range(1, n + 1):
        result *= i 
        sequence.append(result) 
    return sequence

try:
    num = int(input("Enter a positive integer to compute its factorial sequence: ").strip())
    if num < 0:
        raise ValueError("Input must be a positive integer.")
    
    fact_sequence = factorial(num)
    print(f"Factorial sequence up to {num}!: {fact_sequence}")
    
    # Plotting the factorial sequence in graphical form

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, num + 1), fact_sequence, marker='o')  
    plt.title(f'Factorial Sequence up to {num}!')
    plt.xlabel('n') 
    plt.ylabel('n!')
    plt.yscale('log')   
    plt.grid(True)
    plt.show()
    
except ValueError as e:
    print(f"Error: {e}")    

    
