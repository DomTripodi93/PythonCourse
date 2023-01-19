class Furniture:
    def __init__(self, **kwargs):
        self.price = kwargs["price"]
        self.can_sit = kwargs["can_sit"]
        
    def compare_price(self, compare_to):
        if compare_to > self.price:
            return ">"
        elif compare_to < self.price:
            return "<"
        else:
            return "="
            
class Chair(Furniture):
    def __init__(self, **kwargs):
        super().__init__(price = kwargs["price"], can_sit = True)
        
    def compare_price(self):
        if 1000 > self.price:
            return ">"
        elif 1000 < self.price:
            return "<"
        else:
            return "="

definitely_a_chair = Chair(price = 95)
a_table_or_something = Furniture(price = 100, can_sit = False)

print(definitely_a_chair.can_sit)
print(a_table_or_something.can_sit)
