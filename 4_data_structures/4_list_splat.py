
my_number_list = [3, 4, 5, 2, 1, 3, 5]

# my_copy_list = my_number_list
my_copy_list = [*my_number_list]


print("Both lists printed")
print(my_number_list)
print(my_copy_list)


my_number_list[0] = 17

print("\nBoth lists printed after changing the original list")
print(my_number_list)
print(my_copy_list)

my_combined_list = [*my_number_list, *my_copy_list]


print("\nMy combined clone of both lists")
print(my_combined_list)