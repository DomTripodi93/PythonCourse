
my_comma_string = "some, random, set, of, words, separated, by, commas"

print("My comma string variable: my_comma_string")
print(my_comma_string)

my_split_list = my_comma_string.split(", ")

print("\nMy list from splitting the comma string " + 
    "variable: my_comma_string.split(\", \")")
print(my_split_list)

my_rejoined_string = str.join(" ", my_split_list)

print("\nMy string from joining the split list: " + 
    "str.join(\" \", my_split_list)")
print(my_rejoined_string)

print("\nUsing the replace method to remove the commas from our string: " +
    "my_comma_string.replace(\", \", \" \") OR my_comma_string.replace(\",\", \"\")")
print(my_comma_string.replace(", ", " "))
print(my_comma_string.replace(",", ""))
