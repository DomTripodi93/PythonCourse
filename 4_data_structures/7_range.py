
# my_first_range = range(7)
my_first_range = range(0, 7)

# print("My first range: range(7)")
print("My first range: range(0, 7)")
print(my_first_range)
print(*my_first_range)

my_first_range_list = [*my_first_range]
print("\nMy first range as a list: [*my_first_range]")
print(my_first_range_list)

my_second_range = range(3, 7)

print("\nMy second range: range(3, 7)")
print(my_second_range)
print(*my_second_range)

my_first_range_list.extend(my_second_range)

print("\nMy list with both ranges: my_first_range_list.extend(my_second_range)")
print(my_first_range_list)

print("\nThe sum of our range: sum(my_second_range)")
print(sum(my_second_range))

print("\nThe sum of our list: sum(my_first_range_list)")
print(sum(my_first_range_list))
