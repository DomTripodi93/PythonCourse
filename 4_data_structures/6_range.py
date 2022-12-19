
my_first_range = range(5)

print("My first range with from the input of 5")
print(my_first_range)

my_list_to_append_to = []

my_list_to_append_to.extend(my_first_range)

print("\nMy list extended by a range of 5")
print(my_list_to_append_to)


my_second_list_to_append_to = []

my_second_list_to_append_to.extend(range(3, 7))
print("\nMy second list extended by a range of 3, 7")
print(my_second_list_to_append_to)

print("\nThe sum of the elements in my second list extended by a range of 3, 7")
print(sum(my_second_list_to_append_to))


print("\nThe sum of a range of 3, 7")
print(sum(range(3, 7)))
