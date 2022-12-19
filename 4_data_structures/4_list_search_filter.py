combined_list = [8, 5, 7, 4, 4, 2, 2, 8, 5, 4, 4, 2, 2]

print("The full list: combined_list")
print(combined_list)


largest_number = max(combined_list)
print("\nThe largest number in my list: max(combined_list)")
print(largest_number)


smallest_number = min(combined_list)
print("\nThe smallest number in my list: min(combined_list)")
print(smallest_number)


index_of_first_two = combined_list.index(2)
print("\nThe first index of 2 in my list: my_second_list.index(2)")
print(index_of_first_two)


print("\nThe element at that index: my_second_list.index(combined_list.index(" +
      str(index_of_first_two) + "))")
print(combined_list[index_of_first_two])


# broken_index = combined_list.index(20)
check_in_list = 20 in combined_list
print("\nWhether or not 20 is in my list: 20 in combined_list")
print(check_in_list)


check_in_list = 2 in combined_list
print("\nWhether or not 2 is in my list: 2 in combined_list")
print(check_in_list)


my_filtered_list = [list_item for list_item in combined_list if list_item > 4]
print("\nA filtered list of items greater than 4: " +
      "[list_item for list_item in combined_list if list_item > 4]")
print(my_filtered_list)
