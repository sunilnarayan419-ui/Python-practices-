# TO add two numbers 

def get_num(prompt):
    while True: 
        try: 
            return float(input(prompt).strip()) 
        except ValueError: 
            print(f"Invalid input !!") 
num_1 = get_num(f"Enter frist num : ") 
num_2 = get_num(f"Enter second num : ")
 
total = num_1 + num_2 
print(f"Sum of {num_1} and {num_2} = {total:.3f}") 