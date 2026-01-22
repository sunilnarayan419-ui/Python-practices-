# Leap year checker 

class LeapYearChecker:

    def __init__(self, year):
        self.year = year

    def validate_year(self):
        if self.year < 0:
            return "Year cannot be negative."
        return "Year is valid."

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False

    def display_result(self):
        validation_message = self.validate_year()
        if validation_message != "Year is valid.":
            return validation_message

        if self.is_leap_year():
            return f"{self.year} is a leap year."
        else:
            return f"{self.year} is not a leap year." 
        
def main():
    try:
        year = int(input("Enter a year to check if it's a leap year: ").strip())

        leap_year_checker = LeapYearChecker(year)
        print(leap_year_checker.display_result())

    except ValueError:
        print("Invalid input. Please enter a valid year.") 
if __name__ == "__main__":
    main() 