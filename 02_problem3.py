# To check Even/Odd number 

try:
    num = int(input("Enter an integer: ").strip())

    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")

except ValueError:
    print("Please enter a valid integer.")
