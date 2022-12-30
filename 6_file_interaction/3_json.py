import json

json_string = "{\"someKey\": \"some value\"}"

# NoneType
# noneType
print("Our original JSON string")
print(json_string)


output_dictionary = json.loads(json_string)

print("\nOur converted dictionary from our JSON string")
print(output_dictionary)


print("\nThe someKey value in our dictionary")
print(output_dictionary["someKey"])


json_string_output = json.dumps(output_dictionary)


print("\nOur converted JSON string from our dictionary")
print(json_string_output)

file = open("jsonOutput.json", "w")

file.write(json_string_output)
