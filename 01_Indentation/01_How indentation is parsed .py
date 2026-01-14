# How indentation is parsed 
# “Python uses indentation to define code blocks.
# A block starts after : and ends when indentation decreases.”

# example 
x = 7

if x > 5:
    if x < 10:
        print("Between 5 and 10")
    print("Inside first if")

print("Outside all")

# Parsing hierarchy 
# if x > 5:
#     ├─ if x < 10:
#     │   └─ print("Between 5 and 10")
#     └─ print("Inside first if")

# print("Outside all")




