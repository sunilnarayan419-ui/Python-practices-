# Simple Password Checker

class PasswordChecker:
    """This program checks a password"""

    @staticmethod
    def check_password(pwd):
        return pwd == "SunilNarayan"


while True:
    try:
        password = input("Enter your password: ")

        if PasswordChecker.check_password(password):
            print("Entry Granted!! ")
            break
        else:
            print("Please enter correct password !! ")

    except Exception:
        print("Something went wrong !!")
       
        
  
  