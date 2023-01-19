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
            
class Chair(Furniture):
    pass

definitely_a_chair = Chair(price = 95)

print(definitely_a_chair.compare_price(55))
