
my_first_dictionary = {
    "some_num": 7,
    "some_string": "words"
}

my_first_dictionary["new_key"] = "new val"

print("Our whole first dictionary")
print(my_first_dictionary)


print("\nOur some_num value in our dictionary: my_first_dictionary[\"some_num\"]")
print(my_first_dictionary["some_num"])

my_second_dictionary = dict([("key", "value"),("key_int", 8)])
print("\nOur whole second dictionary")
print(my_second_dictionary)

print("\nGetting the keys from our dictionary")
print(dict.keys(my_first_dictionary))
print(my_first_dictionary.keys())

print("\nGetting the keys from our dictionary as a list")
print([*dict.keys(my_first_dictionary)])
print([*my_first_dictionary.keys()])
print(list(my_first_dictionary.keys()))

print("\nOur whole first dictionary before deleting new_key")
print(my_first_dictionary)
del my_first_dictionary["new_key"] 
print("\nOur whole first dictionary after deleting new_key")
print(my_first_dictionary)
