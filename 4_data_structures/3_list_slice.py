
my_number_list = [3, 4, 5, 2, 1, 3, 5]

print("My list in it's original order")
print(my_number_list)

my_number_list.sort()

print("\nMy list after it is sorted")
print(my_number_list)

my_number_list.sort(reverse=True)

print("\nMy list after it is sorted in descending order")
print(my_number_list)

# my_sub_list = my_number_list[0:3]
my_sub_list = my_number_list[:3]

print("\nMy sub-list based on the 4th item at the 3rd index as an upper bound")
print(my_sub_list)


my_sub_list = my_number_list[3:]

print("\nMy sub-list based on the 4th item at the 3rd index as an lower bound")
print(my_sub_list)

#[5, 5, 4, 3, 3, 2, 1]


my_sub_list = my_number_list[3:5]

print("\nMy sub-list based on the 4th item at the 3rd index as an lower bound\n" +
    "and our 6th item at the 5th index as the upper bound")
print(my_sub_list)

