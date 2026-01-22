# currency converter 

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    print(f"Converting {amount} from {from_currency} to {to_currency}...")
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Unsupported currency.")   
    rate = exchange_rates[to_currency] / exchange_rates[from_currency]
    converted_amount = amount * rate    
    return converted_amount
def main():
    exchange_rates = {
        'USD': 1.0,      
        'EUR': 0.85,     
        'JPY': 110.0,    
        'GBP': 0.75,     
        'INR': 74.0      
    }    
    try:
        amount = float(input("Enter the amount to convert: ").strip())
        from_currency = input("Enter the source currency (USD, EUR, JPY, GBP, INR): ").strip().upper()
        to_currency = input("Enter the target currency (USD, EUR, JPY, GBP, INR): ").strip().upper()        
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)        
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")    
    except ValueError as e:
        print(f"Error: {e}")   
        
if __name__ == "__main__":
    main()  