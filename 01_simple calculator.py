# Simple Calculator using python

num_1 = float(input("Enter first number: ").strip())
num_2 = float(input("Enter second number: ").strip()) 

operation = input("Enter operation (+, -, *, /): ").strip() 

if operation == '+':
    result = num_1 + num_2
    print(f"{num_1} + {num_2} = {result:.3f}")  
elif operation == '-':
    result = num_1 - num_2
    print(f"{num_1} - {num_2} = {result:.3f}")  
elif operation == '*':
    result = num_1 * num_2
    print(f"{num_1} * {num_2} = {result:.3f}")  
elif operation == '/':
    if num_2 != 0:
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result:.3f}")  
    else:
        print("Error: Division by zero is not allowed.")    