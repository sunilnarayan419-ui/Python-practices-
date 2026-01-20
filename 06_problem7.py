# to calculate area of circle 

import math

def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius ==0:
        return 0.0  
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2    
try:
    radius = float(input("Enter the radius of the circle: ").strip())
    area = area_of_circle(radius)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")    
except ValueError:
    print("Please enter a valid non-negative numeric value for radius.")    
    
# area of rectangle 

def area_of_rectangle(length, width):
    """Calculate the area of a rectangle given its length and width."""
    if length ==0 or width ==0:
        return 0.0
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width   
try:
    length = float(input("Enter the length of the rectangle: ").strip())
    width = float(input("Enter the width of the rectangle: ").strip())
    area = area_of_rectangle(length, width)
    print(f"The area of the rectangle with length {length} and width {width} is: {area:.2f}")   
except ValueError:
    print("Please enter valid non-negative numeric values for length and width.")   
    
# area of triangle  

def area_of_triangle(base, height):
    """Calculate the area of a triangle given its base and height."""
    if base ==0 or height ==0:
        return 0.0  
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height 

try:
    base = float(input("Enter the base of the triangle: ").strip())
    height = float(input("Enter the height of the triangle: ").strip())
    area = area_of_triangle(base, height)
    print(f"The area of the triangle with base {base} and height {height} is: {area:.2f}")  
except ValueError:
    print("Please enter valid non-negative numeric values for base and height.")    