#  Python program to swap numbers in pairs.

class pair_swap:
    """ A class to swap numbers in pairs within a tuple.
    """ 
    @staticmethod
    def pair_wise_swap(*numbers):
        if len(numbers) % 2 != 0:
            raise ValueError("Even number of values required.")

        swapped = []
        for i in range(0, len(numbers), 2):
            swapped.extend([numbers[i+1], numbers[i]])

        return tuple(swapped) 
def main():
    try:
        input_numbers = input("Enter an even number of integers separated by spaces: ").strip()
        numbers = tuple(float(num) for num in input_numbers.split())

        swapped_numbers = pair_swap.pair_wise_swap(*numbers)
        print(f"Swapped numbers: {swapped_numbers}")

    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main() 