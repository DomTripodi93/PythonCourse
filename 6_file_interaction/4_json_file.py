import json


json_file = open("randomNames.json", "r")

json_string = json_file.read()

# NoneType
# noneType
print("Our original JSON string")
print(json_string)


output_list = json.loads(json_string)

# print("\nOur converted list of dictionaries from our JSON file")
# print(output_list)


print("\nThe first dictionary inside of our list at the index of 0")
print(output_list[0])


json_string_output = json.dumps(output_list)


# print("\nOur converted JSON string from our list")
# print(json_string_output)

file = open("randomNames - Copy.json", "w")

file.write(json_string_output)
