# Multiplication Table Generator 

class MultiplicationTable:
    """ This is Multiplication Table Generator Code """

    def __init__(self, number):
        self.number = number

    def generate_table(self):
        for i in range(1, 11):
            print(f"{self.number} * {i} = {self.number * i}")


try:
    num = float(input("Enter a number: "))
    table = MultiplicationTable(num)
    table.generate_table()

except ValueError:
    print("Something went wrong. Try again")
