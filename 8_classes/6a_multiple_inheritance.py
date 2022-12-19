
class MyConstructableClass:
    def __init__(self, **kwargs):
        self.numeric_attribute = kwargs["numeric_attribute"]
        self.string_attribute = kwargs["string_attribute"]

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


class MyMixin(MyConstructableClass):
    nothing = ""

    # def __init__(self, **kwargs):
    #     super().__init__(
    #         numeric_attribute=100,
    #         string_attribute=kwargs["string_attribute"]
    #     )


class MyInheritedClass(MyConstructableClass):
    def __init__(self, **kwargs):
        super().__init__(
            numeric_attribute=kwargs["numeric_attribute"],
            string_attribute="Inherited String"
        )
        self.test_attribute = kwargs["test_attribute"]

    def compare_to_numeric(self, value_to_compare):
        result = super().compare_to_numeric(value_to_compare)
        if result == "Values are not comparable":
            return str(self.numeric_attribute) + " and " + str(value_to_compare) + \
                " " + result.lower()
        else:
            return str(self.numeric_attribute) + " is " + result.lower() + \
                " " + str(value_to_compare)


class MyMultiInheritedClass(MyInheritedClass, MyMixin):
    def __init__(self, **kwargs):
        super().__init__(
            numeric_attribute=kwargs["numeric_attribute"], test_attribute="test_att")


# my_class_instance = MyInheritedClass(6, "words", "new test value")
# my_class_instance = MyInheritedClass(6, "new test value")
my_class_instance = MyMultiInheritedClass(numeric_attribute=12)

print("\nA view of numeric_attribute, string_attribute and test_attribute on my_class_instance " +
      "instance of MyInheritedClass")
print(my_class_instance.numeric_attribute)
print(my_class_instance.string_attribute)
print(my_class_instance.test_attribute)


print("\nThe result of my_class_instance.compare_to_numeric_plus(17)")
print(my_class_instance.compare_to_numeric(17))

print("\nThe result of my_class_instance.compare_to_numeric_plus([])")
print(my_class_instance.compare_to_numeric([]))
