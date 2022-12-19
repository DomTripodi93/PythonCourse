
class Furniture:
    def __init__(self, **kwargs):
        self.price = kwargs["price"]
        self.can_sit = kwargs["can_sit"]
        self.for_office = kwargs["for_office"]

    def compare_to_numeric(self, value_to_compare):
        try:
            if value_to_compare > self.price:
                return "Greater Than"
            elif value_to_compare < self.price:
                return "Less Than"
            else:
                return "Equal To"
        except:
            return "Values are not comparable"


class OfficeFurniture(Furniture):
    def __init__(self, **kwargs):
        super().__init__(
            price=kwargs["price"],
            can_sit=kwargs["can_sit"],
            for_office=True
        )


class Chair(Furniture):
    def __init__(self, **kwargs):
        super().__init__(
            price=kwargs["price"],
            can_sit=True,
            for_office=kwargs["for_office"]
        )

    def compare_to_numeric(self, value_to_compare):
        result = super().compare_to_numeric(value_to_compare)
        if result == "Values are not comparable":
            return str(self.price) + " and " + str(value_to_compare) + \
                " " + result.lower()
        else:
            return str(self.price) + " is " + result.lower() + \
                " " + str(value_to_compare)


class OfficeChair(Chair, OfficeFurniture):
    def __init__(self, price):
        super().__init__(
            price=price,
            for_office=None
        )


my_class_instance = OfficeChair(75)

print("\nA view of price, can_sit and for_office on my_class_instance " +
      "instance of OfficeChair")
print(my_class_instance.price)
print(my_class_instance.can_sit)
print(my_class_instance.for_office)


print("\nThe result of my_class_instance.compare_to_numeric_plus(17)")
print(my_class_instance.compare_to_numeric(17))

print("\nThe result of my_class_instance.compare_to_numeric_plus([])")
print(my_class_instance.compare_to_numeric([]))
