
menu_items = [
    "cheeseburger:4",
    "fries:3",
    "nuggets:5",
    "chicken sandwich-5",
    "milk shake:2",
    "soda:1"
]

menu_item_dictionaries = []

for item in menu_items:
    # print(item)
    if not ":" in item:
        continue
    item_parts = item.split(":")
    output_item = {
        "item_name": item_parts[0],
        "item_price": item_parts[1]
    }
    menu_item_dictionaries.append(output_item)

print("Loop finished")
print(menu_item_dictionaries)
