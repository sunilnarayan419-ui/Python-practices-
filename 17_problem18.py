# Armstrong number checker 

class ArmstrongChecker:
    @staticmethod
    def is_armstrong(number):
        """Check if a number is an Armstrong number."""
        str_num = str(number)
        num_digits = len(str_num)
        sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
        return sum_of_powers == number
    
    
     
def main():
 try:
        num = int(input("Enter a number to check if it's an Armstrong number: ").strip())   
        if num < 0:
            print("Please enter a non-negative integer.")
            return  
        if ArmstrongChecker.is_armstrong(num):
            print(f"{num} is an Armstrong number.") 
        else:
            print(f"{num} is not an Armstrong number.") 
 except ValueError:
        print("Invalid input. Please enter a valid integer.") 
          
if __name__ == "__main__":
    main()