# Set Data Type 
# unorded collection of unique objects 
# There are two type of sets 
# 1. Sets = mutable and new elements can be added once sets are defiend 

basket = { 'apple', 'orange' , 'apple' , 'pear' , 'orange', 'banana' 
           } 
# print(basket)  # duplicates will be removed 
a = set('abracadabra') 
# print(a)  # unique letters in a 
a.add('z') 
print(a) 

# 2. Frozen Sets = immutable and new elements cannot added after its defined.

b = frozenset("SunilNarayan") 
print(b) 
cities = frozenset(["vadodara" , "indore" , "hyderabad" , "anand"]) 
print(cities) 
cities = frozenset({"vadodara" , "indore" , "hyderabad" , "anand"})
print(cities) 

