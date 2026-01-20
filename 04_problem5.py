# Simple interest calculator 

try:
    principal = float(input("Enter the principal amount: ").strip())
    rate = float(input("Enter the annual interest rate (in %): ").strip())  
    time = float(input("Enter the time in years: ").strip())

    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

# ---------------------------------------------------------------
# Display the results
    print(f"Simple Interest: {simple_interest:.2f}")
    print(f"Total Amount after {time} years: {total_amount:.2f}") 
# ---------------------------------------------------------------       
except ValueError:
    print("Please enter valid numeric values.")   