import json

json_test_string = "{\"someKey\": \"Some Value\"}"

json_result = json.loads(json_test_string)

print("Dictionary created by parsing JSON")
print(json_result)

print("\nValue accessed by a key in the dictionary created by parsing JSON")
print(json_result["someKey"])

json_reverted = json.dumps(json_result)

print("\nMy dictionary converted to a JSON string")
print(json_reverted)
