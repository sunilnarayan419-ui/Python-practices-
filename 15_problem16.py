# This program generates the first n Fibonacci numbers and plots them using matplotlib.

import matplotlib.pyplot as plt

def fibonacci(n):
    """Generate a list containing the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence


def main():
    try:
        n = int(input("Enter the number of Fibonacci numbers to generate: ").strip())
        if n < 0:
            print("Please enter a non-negative integer.")
            return

        fib_sequence = fibonacci(n)
        print(f"The first {n} Fibonacci numbers are: {fib_sequence}")

        if n > 0:
            plt.plot(range(n), fib_sequence, marker='o')
            plt.title(f'First {n} Fibonacci Numbers')
            plt.xlabel('Index')
            plt.ylabel('Fibonacci Number')
            plt.yscale('log')  
            plt.grid()
            plt.show()

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
