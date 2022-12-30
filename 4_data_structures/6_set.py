
my_number_list = [17, 4, 5, 2, 1, 3, 5, 3, 4, 5, 2, 1, 3, 5]

# my_number_list.sort()


print("Our whole starting list: my_number_list")
print(my_number_list)

my_first_set = set(my_number_list)

print("\nOur first set, based on the number list: set(my_number_list)")
print(my_first_set)


my_deduplicated_list = [*my_first_set]

print("\nOur new list with no duplicates: [*my_first_set]")
print(my_deduplicated_list)


print("\nOur new list with no duplicates in one line: [*set(my_number_list)]")
print([*set(my_number_list)])


set_contains_five = 5 in my_first_set

print("\nWhether or not our set contains a 5: 5 in my_first_set")
print(set_contains_five)
