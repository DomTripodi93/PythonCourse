import datetime

my_first_dictionary = {
    "key": "value",
    "some_date": datetime.datetime(2023, 5, 22)
}

print(
    "The value of the item assigned to the key \"some_date\": my_first_dictionary[\"some_date\"]")
print(my_first_dictionary["some_date"])

print(
    "\nThe value of the item assigned to the key \"key\": my_first_dictionary[\"key\"]")
print(my_first_dictionary["key"])

my_first_dictionary["new_val"] = 257

print(
    "\nThe value of the item assigned to the key \"new_val\": my_first_dictionary[\"new_val\"]")
print(my_first_dictionary["new_val"])

print(
    "\nThe keys of our dictionary: dict.keys(my_first_dictionary)")
print(dict.keys(my_first_dictionary))
print(my_first_dictionary.keys())
print(list(my_first_dictionary.keys()))
print([*my_first_dictionary.keys()])

del my_first_dictionary["new_val"]

print(
    "\nThe dictionary after deleting the key \"new_val\": del my_first_dictionary")
# print(my_first_dictionary["new_val"])
print(my_first_dictionary)

my_second_dictionary = dict([("some_key", "some_val")])

print(
    "\nThe second dictionary created with the dict constructor: dict([(\"some_key\", \"some_val\")])")
# print(my_first_dictionary["new_val"])
print(my_second_dictionary)

