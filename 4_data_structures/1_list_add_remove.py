import datetime

my_first_list = [
    5,
    "some words",
    datetime.datetime(2023,6,15),
    True,
    None,
    True
]

print("my_first_list")
print(my_first_list)

print("\nAccessing the first item at the index of 0: my_first_list[0]")
print(my_first_list[0])

print("\nAccessing the third item at the index of 2: my_first_list[2]")
print(my_first_list[2])


#This causes and "IndexError: list index out of range"
# print("\nAccessing the sixth item at the index of 5: my_first_list[5]")
# print(my_first_list[5])


my_first_list[0] = 7

print("\nmy_first_list after setting the first item at the index of 0 to 7")
print(my_first_list)

my_first_list.append(12)

print("\nmy_first_list after appending a 12")
print(my_first_list)

# my_first_list.pop()
# my_removed_value = my_first_list.pop() #Returns removed value
# print("\nmy_first_list after popping the last item off of the list")
# print(my_first_list)


# my_removed_value = my_first_list.pop(3) #Returns removed value
# print("\nmy_first_list after popping the last fourth item at the index of 3 off of the list")
# print(my_first_list)

my_removed_value = my_first_list.remove(True) #Returns NoneType value
print("\nmy_first_list after removing the first instance of True from the list: my_first_list.remove(True)")
print(my_first_list)

print("\nThe value removed from my_first_list: my_removed_value")
print(my_removed_value)
