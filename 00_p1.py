food = str(input(f"Enter your food : ")) 
num_food = int(input(f"Enter how many item do you want : "))
price = float(input(f"Enter the price of food : ")) 
total = num_food*price

print("*******YOUR BILL SIR********") 

print(f"Your food {food}") 
print(f"You bought {num_food} items of {food}") 
print(f"Your total is ${total:.3f}") 

print("THANK YOU SIR !!" )

print("****************************") 
