
menu_items = [
    "cheeseburger:4",
    "fries:4",
    "nuggets:4",
    "chicken sandwich-4",
    "milk shake:4",
    "soda:4"
]

cart_dictionaries = []
cart_total = 0

for item in menu_items:
    print(item)
    if not ":" in item:
        continue
    item_parts = item.split(":")
    output_item = {
        "item_name": item_parts[0],
        "item_price": int(item_parts[1])
    }
    if cart_total + output_item["item_price"] < 10:
        cart_total += output_item["item_price"]
        cart_dictionaries.append(output_item)
    else:
        break

print("Loop finished")
print(cart_dictionaries)
