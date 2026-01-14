# Example

class ExampleClass:
    # Constructor
    def __init__(self):
        self.name = "example"

    def someFunction(self, a):
        if a > 5:
            return True
        else:
            return False

    def separateFunction(self, b):
        for i in b:
            if i == 1:
                return True
        return False   # runs after loop finishes


# Creating object
obj = ExampleClass()

print(obj.someFunction(10))
print(obj.separateFunction([2, 3, 5, 6, 1]))
