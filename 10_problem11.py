# temperature converter 

def convert_temp(amount, from_unit, to_unit):
    print(f"Converting {amount} from {from_unit} to {to_unit}...") 
    if from_unit == to_unit:
        return amount
    if from_unit == 'C':
        if to_unit == 'F':
            return (amount * 9/5) + 32
        elif to_unit == 'K':
            return amount + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (amount - 32) * 5/9
        elif to_unit == 'K':
            return (amount - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return amount - 273.15
        elif to_unit == 'F':
            return (amount - 273.15) * 9/5 + 32
    raise ValueError("Unsupported temperature unit.") 

def main():
    try:
        amount = float(input("Enter the temperature to convert: ").strip())
        from_unit = input("Enter the source unit (C, F, K): ").strip().upper()
        to_unit = input("Enter the target unit (C, F, K): ").strip().upper()        
        converted_amount = convert_temp(amount, from_unit, to_unit)        
        print(f"{amount} {from_unit} is equal to {converted_amount:.2f} {to_unit}.")    
    except ValueError as e:
        print(f"Error: {e}")  
        
if __name__ == "__main__":
    main()   