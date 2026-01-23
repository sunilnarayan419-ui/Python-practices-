# Palindrome number checker 

class PalindromeChecker:
    @staticmethod
    def is_palindrome(number):
        """Check if a number is a palindrome."""
        str_num = str(number)
        return str_num == str_num[::-1]


def main():
    try:
        num = int(input("Enter a number to check if it's a palindrome: ").strip())

        if num < 0:
            print("Please enter a non-negative integer.")
            return

        if PalindromeChecker.is_palindrome(num):
            print(f"{num} is a palindrome.")
        else:
            print(f"{num} is not a palindrome.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
