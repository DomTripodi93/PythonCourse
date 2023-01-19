
class MyFirstClass:
    def __init__(self, **kwargs):
        self.my_class_attribute = kwargs["my_class_attribute"]
        print("My first class is initialized")
        print(self.my_class_attribute)


my_first_class_instance = MyFirstClass(my_class_attribute=10)
my_second_class_instance = MyFirstClass(my_class_attribute=5)

my_first_class_instance.my_class_attribute += 7

print("my_class_attribute on my_first_class_instance")
print(my_first_class_instance.my_class_attribute)

print("\nmy_class_attribute on my_second_class_instance")
print(my_second_class_instance.my_class_attribute)
