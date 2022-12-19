
class MyConstructableClass:
    def __init__(self, numeric_attribute, string_attribute):
        self.numeric_attribute = numeric_attribute
        self.string_attribute = string_attribute

    def compare_to_numeric(self, value_to_compare):
        try:
            if value_to_compare > self.numeric_attribute:
                return "Greater Than"
            elif value_to_compare < self.numeric_attribute:
                return "Less Than"
            else:
                return "Equal To"
        except:
            return "Values are not comparable"

class MyInheritedClass(MyConstructableClass):
    # test_attribute = 7
    def __init__(self, numeric_attribute, string_attribute, test_attribute):
        self.numeric_attribute = numeric_attribute
        self.string_attribute = string_attribute
        self.test_attribute = test_attribute


# my_class_instance = MyInheritedClass(6, "words")
my_class_instance = MyInheritedClass(6, "words", "new test value")

print("\nA view of numeric_attribute, string_attribute and test_attribute on my_class_instance " +
      "instance of MyInheritedClass")
print(my_class_instance.numeric_attribute)
print(my_class_instance.string_attribute)
print(my_class_instance.test_attribute)


print("\nThe result of my_class_instance.compare_to_numeric(17)")
print(my_class_instance.compare_to_numeric(17))

print("\nThe result of my_class_instance.compare_to_numeric([])")
print(my_class_instance.compare_to_numeric([]))
