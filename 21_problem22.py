# To Calculate Work 

import math
 
class CalculateWork: 
    """ This is program to calculate work in physics. """ 
    
    def __init__(self, force, displacement, theta): 
        self.force = force 
        self.displacement = displacement 
        self.theta = theta 
        
    def Calcutate_Work(self): 
        theta_red = math.radians(self.theta) 
        work = self.force * self.displacement * math.cos(theta_red)
        
        if self.theta < 90: 
            print(f"Work done is Positive {work:.3f}") 
        elif self.theta == 90:
            print("Work done is Zero") 
        else: 
            print(f"Work done is Negative {work:.3f}") 
            
try: 
    force = float(input("Enter force : ")) 
    displacement = float(input("Enter displacement: ")) 
    theta = float(input("Enter theta (in degree): ")) 
    
    obj = CalculateWork(force, displacement, theta) 
    obj.Calcutate_Work() 
except ValueError: 
    print("Something went wrong. Please check your input!!") 
