#  Arithmetic Operations 

try: 
    num_1 = float(input(f"Enter your first number : ")) 
    num_2 = float(input(f"Enter your second number : ")) 

except ValueError:
 print(f"Please enter valid numbers !") 
 exit() 
 

print(f"Choose Operation : ")
print(f"1. Addition (+)") 
print(f"2. Subtraction (-)") 
print(f"3. Multiplication (*)")  
print(f"4. Division (/)") 
print(f"5. Floor Division (//)") 
print(f"6. Modulus (%)") 
print(f"7. Power (**)") 

try:
    choice = int(input(f"Enter your choice(1-7) : ")) 
except ValueError:
 print(f"Please enter valid numbers !") 
 exit() 


if choice == 1:
     print(f"Addition = {num_1 + num_2}") 
elif choice == 2:
     print(f"Subtraction = {num_1 - num_2}") 
elif choice == 3:
     print(f"Multiplication = {num_1 * num_2}") 
elif choice == 4:
    if num_2 != 0:
      print(f"Division = {num_1 / num_2}") 
    else: 
        print(f"Error : Division by zero !") 
elif choice == 5:
    if num_2 != 0:
      print(f"Floor Division = {num_1 // num_2}") 
    else: 
        print(f"Error : Division by zero ! ")
elif choice == 6:
    if num_2 != 0:
      print(f"Modulus = {num_1 % num_2}") 
    else: 
       print(f"Error : Division by zero !")
elif choice == 7:
     print(f"Power = {num_1 ** num_2}") 
else: 
     print(f"Invalid choice !") 


