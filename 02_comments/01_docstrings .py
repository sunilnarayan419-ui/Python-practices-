# Docstrings = unlike regular comments 
# we can access them programmatically 

# Example 

# Docstrings: unlike regular comments,
# they can be accessed programmatically

def func():
    """This is a function that does nothing at all"""
    return


# Accessing the docstring using __doc__
print(func.__doc__)

# Using help() to view documentation
help(func)


# Write documentation using docstring 

def hello(name):
    """
    Greet someone .
    Print a greeting ("Hello") for the person with the given name. 
    
    """ 
    
    print("Hello"+ name) 
class Greeter: 
    """
    An object used to greet people. 
    It contains multiple greeting functions for several languages 
    and times of the day.
    
    """