
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