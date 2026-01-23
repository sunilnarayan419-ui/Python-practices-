# sum of digits 

class DigitSumCalculator:
    @staticmethod
    def sum_of_digits(number):
        """Calculate the sum of the digits of a number."""
        return sum(int(digit) for digit in str(abs(number)))    
def main():
    try:
        num = int(input("Enter a number to calculate the sum of its digits: ").strip())   
        result = DigitSumCalculator.sum_of_digits(num)
        print(f"The sum of the digits of {num} is: {result}") 
    except ValueError:
        print("Invalid input. Please enter a valid integer.")   
if __name__ == "__main__":
    main() 