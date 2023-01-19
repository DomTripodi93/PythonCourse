
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


my_first_class_instance = MyFirstClass(numeric_attribute=10)
my_second_class_instance = MyFirstClass(numeric_attribute=5)

print("The result of compare_to_attribute for 7 on " +
      "my_second_class_instance: my_second_class_instance.compare_to_attribute(7)")
print(my_second_class_instance.compare_to_attribute(7))
