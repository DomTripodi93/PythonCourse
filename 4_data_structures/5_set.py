my_duplicate_list = [8, 5, 7, 4, 4, 2, 2, 8, 5, 4, 4, 2, 2]

print("A list with duplicates: my_duplicate_list")
print(my_duplicate_list)


my_first_set = set(my_duplicate_list)
print("\nA set created from the list with duplicates: set(my_duplicate_list)")
print(my_first_set)


my_deduplicated_list = [*my_first_set]
print("\nA list created from that set: [*my_first_set]")
print(my_deduplicated_list)


my_quick_deduplicated_list = [*set(my_duplicate_list)]
print(
    "\nA list created from combining those techniques: [*set(my_duplicate_list)]")
print(my_quick_deduplicated_list)


includes_eight = 8 in my_first_set
print(
    "\nThe result of searching for 8 in our set: 8 in my_first_set")
print(includes_eight)


includes_eight = 80 in my_first_set
print(
    "\nThe result of searching for 80 in our set: 80 in my_first_set")
print(includes_eight)
