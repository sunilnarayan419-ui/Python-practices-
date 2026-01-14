# Tuple data type 
# elements and size can be changed 
# tuples enclosed in () and cannot be updated 
# are immutable 

# Tuple example (immutable data type)

my_tuple = (123, 'hello')
tuple_1 = ('world',)   # single-element tuple needs a comma

print(my_tuple)
print(my_tuple[0])
print(my_tuple + tuple_1)

# my_tuple[1] = 'update'  #  TypeError: tuple does not support item assignment
print(my_tuple)
