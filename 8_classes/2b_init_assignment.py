class Furniture:
    def __init__(self, **kwargs):
        self.price = kwargs["price"]

some_chair_or_something = Furniture(price = 95)

some_kind_of_table = Furniture(price = 115)

print(some_chair_or_something.price == some_kind_of_table.price)
