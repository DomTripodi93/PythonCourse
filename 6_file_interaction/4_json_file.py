import json

json_file = open("random_names.json")

json_test_string = json_file.read()

json_result = json.loads(json_test_string)

print("Dictionary created by parsing JSON: json.loads(json_test_string)[0]")
print(json_result[0])

print("\nValue accessed by a key in the dictionary created by parsing JSON: json_result[0][\"first_name\"]")
print(json_result[0]["first_name"])

json_reverted = json.dumps(json_result)
json_write = open("random_names_copy.json", "w")
json_write.write(json_reverted)
