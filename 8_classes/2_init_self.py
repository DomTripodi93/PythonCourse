
class MyFirstClass:
    # class_attribute = 7
    def __init__(self):
        # class_attribute = 5
        self.class_attribute = 5
        print("constructor called")


my_class_instance = MyFirstClass()

print("\nA view of class_attribute on my_class_instance instance of MyFirstClass")
print(my_class_instance.class_attribute)


class MyConstructableClass:
    def __init__(self, numeric_attribute, string_attribute):
        self.numeric_attribute = numeric_attribute
        self.string_attribute = string_attribute


my_class_instance = MyConstructableClass(6, "words")

print("\nA view of numeric_attribute and string_attribute on my_class_instance " +
      "instance of MyConstructableClass")
print(my_class_instance.numeric_attribute)
print(my_class_instance.string_attribute)
