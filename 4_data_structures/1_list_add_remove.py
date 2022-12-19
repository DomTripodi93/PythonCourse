import datetime

my_first_list = [
    2,
    False,
    datetime.datetime(2023, 5, 20),
    False,
    "words"
]

print("The first item at the index of 0: my_first_list[0]")
print(my_first_list[0])

print("\nThe third item at the index of 2: my_first_list[2]")
print(my_first_list[2])
# print(my_first_list[4])


my_first_list[0] = 7

print("\nAfter changing the first item at the index of 0: my_first_list")
print(my_first_list)


my_first_list.append("new value")

print("\nThe 5th item in the list, at the index of 4: my_first_list[4]")
print(my_first_list[4])


# my_first_list.pop()
popped_list_item = my_first_list.pop()

print("\nAfter removing the last item with the pop method: my_first_list.pop()")
print(my_first_list)


print("\nThe list item that was popped off of the list by the pop method: my_first_list.pop()")
print(popped_list_item)


my_first_list.pop(2)

print("\nAfter removing the 3rd item at the index of 2 with the pop method: my_first_list.pop(2)")
print(my_first_list)


# Remove's the first item in the list that matches the value
my_first_list.remove(False)

print("\nAfter removing the first instance of False with the remove method: my_first_list.remove(False)")
print(my_first_list)
