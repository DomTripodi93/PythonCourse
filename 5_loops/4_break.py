menu_items = [
    "large:fry:7",
    "small:fry:5",
    "single:burger:5",
    "double:burger:6",
    "small:nuggets:4",
    "large:nuggets:6"
]

menu_dict_list = []
total = 0

for item in menu_items:
    item_parts = item.split(":")
    dict_to_add = {
        "size": item_parts[0],
        "item": item_parts[1],
        "price": item_parts[2]
    }
    # total += int(dict_to_add["price"])
    if (total_cost := total + int(dict_to_add["price"])) > 20:
        break
    total = total_cost
    menu_dict_list.append(dict_to_add)

print("\nResulting menu dictionary: menu_dict_list")
print(menu_dict_list)

print("\nTotal cost of items: total")
print(total)
