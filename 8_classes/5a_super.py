
class MyFirstClass:
    def __init__(self, **kwargs):
        self.numeric_attribute = kwargs["numeric_attribute"]

    def compare_to_attribute(self, value_to_compare):
        if value_to_compare > self.numeric_attribute:
            return "Greater than"
        elif value_to_compare < self.numeric_attribute:
            return "Less than"
        else:
            return "Equal"


class MyInheritingClass(MyFirstClass):
    def compare_to_attribute(self, value_to_compare):
        original_response = super().compare_to_attribute(value_to_compare)
        return str(value_to_compare) + " is " + original_response.lower() + \
            " compared to " + str(self.numeric_attribute)
        # if value_to_compare > self.numeric_attribute:
        #     return ">"
        # elif value_to_compare < self.numeric_attribute:
        #     return "<"
        # else:
        #     return "="

    def super_compare(self, value_to_compare):
        return super().compare_to_attribute(value_to_compare)


# my_first_class_instance = MyFirstClass(numeric_attribute=5)
my_second_class_instance = MyInheritingClass(numeric_attribute=5)

# print("The result of compare_to_attribute for 7 on " +
#       "my_first_class_instance: my_first_class_instance.compare_to_attribute(7)")
# print(my_first_class_instance.compare_to_attribute(7))

print("\nThe result of compare_to_attribute for 7 on " +
      "my_second_class_instance: my_second_class_instance.compare_to_attribute(7)")
print(my_second_class_instance.compare_to_attribute(7))

print("\nThe result of compare_to_attribute for 7 on " +
      "my_second_class_instance: my_second_class_instance.super_compare(7)")
print(my_second_class_instance.super_compare(7))
