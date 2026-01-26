# To Calculate Gravitational Force

class GravitationalForce:
    """This program calculates gravitational force using Newton's Law"""

    def __init__(self, gravitational_constant, mass1, mass2, radius):
        self.G = gravitational_constant
        self.m1 = mass1
        self.m2 = mass2
        self.r = radius

    def calculate_force(self):
        force = self.G * self.m1 * self.m2 / (self.r ** 2)
        return force


try:
    G = 6.674e-11   # gravitational constant
    m1 = float(input("Enter mass of first body (kg): "))
    m2 = float(input("Enter mass of second body (kg): "))
    r = float(input("Enter distance between bodies (m): "))

    obj = GravitationalForce(G, m1, m2, r)
    result = obj.calculate_force()

    print(f"Gravitational Force = {result:.3e} N")

except ValueError:
    print("Something went wrong. Please check your input!!")
