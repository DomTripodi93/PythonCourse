
my_first_tuple = (1, 3, 5)

print("Our whole tuple before attempting to change it")
print(my_first_tuple)

# del my_first_tuple[0] # TypeError: 'tuple' object doesn't support item deletion
# my_first_tuple[1] = 7 # TypeError: 'tuple' object does not support item assignment
# my_first_tuple.append(10) # AttributeError: 'tuple' object has no attribute 'append'

my_first_tuple = (3, 2, 1)

print("\nOur whole tuple after attempting to change it")
print(my_first_tuple)


my_int_looks_like_a_tuple = (4)
my_tuple_with_one_element = (4,)


print("My two attempts at creating a tuple with one member")
print(my_int_looks_like_a_tuple)
print(my_tuple_with_one_element)
