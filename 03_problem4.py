# positive/Negative Number Checker 

try:
    num = float(input("Enter a number: ").strip())  
    
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.") 
except ValueError:
    print("Please enter a valid number.")   