
my_number_list = [17, 4, 5, 2, 1, 3, 5, 3, 4, 5, 2, 1, 3, 5]

print("Our whole starting list: my_number_list")
print(my_number_list)


print("\nThe maximum value inside of our list: max(my_number_list)")
print(max(my_number_list))


print("\nThe minimum value inside of our list: min(my_number_list)")
print(min(my_number_list))


index_of_five = my_number_list.index(5)

print("\nThe index of the first 5 in our list: my_number_list.index(5)")
print(index_of_five)


# index_of_ten = my_number_list.index(10)

# print("\nThe index of the first 10 in our list: my_number_list.index(10)")
# print(index_of_ten)
# ValueError: 10 is not in list

list_has_ten = 10 in my_number_list

print("\nWhether or not 10 is in our list: 10 in my_number_list")
print(list_has_ten)



my_filtered_list = [item for item in my_number_list if item > 3]

print("\nItems greater than 3 in our list: " + 
    "[item for item in my_number_list if item > 3]")
print(my_filtered_list)
