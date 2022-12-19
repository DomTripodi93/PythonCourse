menu_items = [
    "large:fry",
    "small:fry",
    "single:burger",
    "double:burger",
    "chicken sandwich",
    "small:nuggets",
    "large:nuggets"
]

menu_dict_list = []

for item in menu_items:
    if ":" not in item:
        continue
    item_parts = item.split(":")
    print(item_parts)
    menu_dict_list.append({
        "size": item_parts[0],
        "item": item_parts[1]
    })

print("\nResulting menu dictionary: menu_dict_list")
print(menu_dict_list)
