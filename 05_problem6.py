# EMI calculator 

try:
    principal = float(input("Enter the principal loan amount: ").strip())
    annual_rate = float(input("Enter the annual interest rate (in %): ").strip())
    time_years = float(input("Enter the loan tenure in years: ").strip())

    if principal <= 0 or time_years <= 0:
        raise ValueError
        

    monthly_rate = annual_rate / (12 * 100)
    total_payments = int(time_years * 12)

    if monthly_rate == 0:
        emi = principal / total_payments
    else:
        emi = (principal * monthly_rate * (1 + monthly_rate) ** total_payments) / \
              ((1 + monthly_rate) ** total_payments - 1)

    print(f"Your monthly EMI is: $ {emi:.2f}")

except ValueError:
    print("Please enter valid positive numeric values.")
