
class MyFirstClass:
    my_class_attribute = 7


my_first_class_instance = MyFirstClass()
my_second_class_instance = MyFirstClass()

my_first_class_instance.my_class_attribute += 7

print("my_class_attribute on my_first_class_instance")
print(my_first_class_instance.my_class_attribute)

print("\nmy_class_attribute on my_second_class_instance")
print(my_second_class_instance.my_class_attribute)
