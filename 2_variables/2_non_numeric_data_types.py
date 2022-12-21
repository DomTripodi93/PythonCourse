import datetime

my_first_string = "hello world"
my_first_string = "hello" + \
    " world"

print("Type of text")
print(type(my_first_string))


my_first_date = datetime.datetime(2023, 5, 20)

print("\nType of date")
print(type(my_first_date))

# my_second_date = datetime.datetime.strptime("2022-12-25", "%Y-%m-%d")
my_second_date = datetime.datetime.strptime("22-12-25", "%y-%m-%d")
print("\nDate parsed from string")
print(my_second_date)


my_first_boolean = False
print("\nType of true/false")
print(type(my_first_boolean))


my_first_none_type = None
print("\nType of None")
print(type(my_first_none_type))




first_assigned, second_assigned = 5, 10

print("\nMultiple assignment")
print(first_assigned)
print(second_assigned)
