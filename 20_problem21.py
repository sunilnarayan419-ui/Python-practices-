# Power Calculator 

class PowerCalculator: 
    """This Program Calculate Power""" 
    def __init__(self , base,exponent): 
        self.base = base 
        self.exponent = exponent 
        
    def Calculate_power(self): 
        result = self.base ** self.exponent 
        print(f"{self.base} ^ {self.exponent} = {result}")  
        
try: 
    base = float(input("Enter Base: ")) 
    exponent = float(input("Enter exponent: ")) 
    
    calc = PowerCalculator(base , exponent) 
    calc.Calculate_power() 
except ValueError: 
    print("Something went wrong. Try again!!")  
        