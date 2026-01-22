# age calculator 

class AgeCalculator:

    def __init__(self, birth_year, current_year):
        self.birth_year = birth_year
        self.current_year = current_year

    def validate_years(self):
        if self.birth_year > self.current_year:
            return "Birth year cannot be greater than current year."
        if self.birth_year < 0 or self.current_year < 0:
            return "Years cannot be negative."
        return "Years are valid."

    def calculate_age(self):
        return self.current_year - self.birth_year

    def display_age(self):
        validation_message = self.validate_years()
        if validation_message != "Years are valid.":
            return validation_message

        age = self.calculate_age()
        return f"You are {age} years old."


def main():
    try:
        birth_year = int(input("Enter your birth year: ").strip())
        current_year = int(input("Enter the current year: ").strip())

        age_calculator = AgeCalculator(birth_year, current_year)
        print(age_calculator.display_age())

    except ValueError:
        print("Invalid input. Please enter valid years.")


if __name__ == "__main__":
    main()
