my_second_list = [4, 2, 5, 4, 8, 2]
my_second_list.sort()

print("\nAfter sorting with the sort method: my_second_list.sort()")
print(my_second_list)


my_second_list.sort(reverse=True)

print("\nAfter sorting in reverse with the sort method: my_second_list.sort(reverse=True)")
print(my_second_list)


print(
    "\nA slice up to but not including the 4th element at the index of 3: my_second_list[0:3]")
print(my_second_list[0:3])
print(my_second_list[:3])

print(
    "\nA slice starting from the 4th element at the index of 3: my_second_list[3:6]")
print(my_second_list[3:6])
print(my_second_list[3:])

print(
    "\nA slice from the 2nd element up to but not including the 6th element: my_second_list[1:5]")
print(my_second_list[1:5])

list_equal = my_second_list
print("\nmy_second_list and list_equal before setting the third item to the value 15")
my_second_list[2] = 15
print(list_equal)
print(my_second_list)

print("\nmy_second_list and list_equal after setting the third item to the value 15")
print(list_equal)
print(my_second_list)


list_clone = [*my_second_list]
my_second_list[2] = 12

print("\nVariadic / splat / spread clone of my_second_list: [*my_second_list]")
combined_list = [*list_clone, *my_second_list]

print(
    "\nVariadic combination of list_clone and my_second_list: [*list_clone, *my_second_list]")
print(combined_list)
print(list_equal)
print(my_second_list)
