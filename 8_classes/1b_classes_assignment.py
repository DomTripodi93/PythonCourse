class Furniture:
    price = 12

some_chair_or_something = Furniture()

some_chair_or_something.price = 5

print(some_chair_or_something.price == Furniture.price)
