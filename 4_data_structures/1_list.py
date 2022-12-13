import datetime

my_first_list = [
    2,
    False,
    datetime.datetime(2022, 12, 20),
    False,
    "words"
]

print("This is the first item at the index of 0")
print(my_first_list[0])

print("\nThis is the third item at the index of 2")
print(my_first_list[2])
# print(my_first_list[4])


my_first_list[0] = 7

print("\nThis is the list, after changing the first item at the index of 0")
print(my_first_list)


my_first_list.append("new value")

print("\nThis is the 5th item in the list, at the index of 0")
print(my_first_list[4])


# my_first_list.pop()
popped_list_item = my_first_list.pop()

print("\nThis is the list, after removing the last item with the pop method")
print(my_first_list)


print("\nThis is the list item that was poped off of the listby the pop method")
print(popped_list_item)


my_first_list.pop(2)

print("\nThis is the list, after removing the 3rd item at the index of 2 with the pop method")
print(my_first_list)


# Remove's the first item in the list that matches the value
my_first_list.remove(False)

print("\nThis is the list, after removing the first instance of False with the remove method")
print(my_first_list)


my_second_list = [4, 2, 5, 4, 8, 2]
my_second_list.sort()

print("\nThis is the second list, after sorting with the sort method")
print(my_second_list)


my_second_list.sort(reverse=True)

print("\nThis is the second list, after sorting in reverse with the sort method")
print(my_second_list)
