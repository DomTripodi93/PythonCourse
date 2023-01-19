class Furniture:
    def __init__(self, **kwargs):
        self.price = kwargs["price"]
        
    def compare_price(self, compare_to):
        if compare_to > self.price:
            return ">"
        elif compare_to < self.price:
            return "<"
        else:
            return "="

some_chair_or_something = Furniture(price = 95)

print(some_chair_or_something.compare_price(55))
print(some_chair_or_something.compare_price(95))
print(some_chair_or_something.compare_price(105))
