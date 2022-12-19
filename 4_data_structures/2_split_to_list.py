string_to_split = "something, with, a, lot, of, commas"

print("The original string: string_to_split")
print(string_to_split)


list_from_split = string_to_split.split(", ")
print("\nThe list created by splitting the string: string_to_split.split(\", \")")
print(list_from_split)


string_rejoined = str.join("-", list_from_split)
print("\nThe list joined back together by a \"-\": str.join(\"-\", list_from_split)")
print(string_rejoined)


print("\nThe string reconstructed in the same way without split: str.replace(string_to_split, \", \", \"-\")")
print(str.replace(string_to_split, ", ", "-"))
