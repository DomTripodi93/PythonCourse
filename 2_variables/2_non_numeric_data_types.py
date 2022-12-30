# from datetime import datetime
import datetime

my_first_string = "hello world"
my_first_string = "hello" + \
    " world"

print("My first and second hello world string variables")
print(type(my_first_string))
print(my_first_string)


# my_first_date = datetime.datetime(2023, 5, 17)
my_first_date = datetime.datetime.strptime("2023-5-17", "%Y-%m-%d")

print("\nMy first datetime variable")
print(type(my_first_date))
print(my_first_date)


my_first_date = datetime.date(2023, 5, 17)
print("\nMy first date variable")
print(type(my_first_date))
print(my_first_date)


my_first_boolean = False
print("\nMy first boolean variable")
print(type(my_first_boolean))
print(my_first_boolean)


my_first_nonetype = None
print("\nMy first NoneType variable")
print(type(my_first_nonetype))
print(my_first_nonetype)


my_first_multi, my_second_multi = 5, 6

print("\nmy_first_multi and my_second_multi variables from multiple assignment")
print(my_first_multi)
print(my_second_multi)
