# grade calculator 

class GradeCalculator:

    def __init__(self, total_marks, obtained_marks):
        self.total_marks = total_marks
        self.obtained_marks = obtained_marks

    def validate_marks(self):
        if self.obtained_marks > self.total_marks:
            return "Obtained marks cannot be greater than total marks."
        if self.total_marks <= 0 or self.obtained_marks < 0:
            return "Marks must be positive and total marks must be greater than zero."
        return "Marks are valid."

    def calculate_percentage(self):
        return (self.obtained_marks / self.total_marks) * 100

    def display_grade(self):
        validation_message = self.validate_marks()
        if validation_message != "Marks are valid.":
            return validation_message

        percentage = self.calculate_percentage()
        return f"Your grade percentage is {percentage:.2f}%." 
    
def main():
    try:
        total_marks = float(input("Enter the total marks: ").strip())
        obtained_marks = float(input("Enter the obtained marks: ").strip())

        grade_calculator = GradeCalculator(total_marks, obtained_marks)
        print(grade_calculator.display_grade())

    except ValueError:
        print("Invalid input. Please enter valid marks.") 
if __name__ == "__main__":
    main() 