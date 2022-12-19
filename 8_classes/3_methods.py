

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
            # elif value_to_compare == self.numeric_attribute:
            else:
                return "Equal To"
            # else:
            #     return "Values are not comparable"
        except:
            return "Values are not comparable"



my_class_instance = MyConstructableClass(6, "words")

print("\nA view of numeric_attribute and string_attribute on my_class_instance " +
      "instance of MyConstructableClass")
print(my_class_instance.numeric_attribute)
print(my_class_instance.string_attribute)


print("\nThe result of my_class_instance.compare_to_numeric(17)")
print(my_class_instance.compare_to_numeric(17))

print("\nThe result of my_class_instance.compare_to_numeric([])")
print(my_class_instance.compare_to_numeric([]))
