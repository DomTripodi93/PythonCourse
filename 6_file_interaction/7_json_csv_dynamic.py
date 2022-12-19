import json

json_file = open("dynamic_json.json")

json_test_string = json_file.read()

json_result = json.loads(json_test_string)

headers = json_result[0].keys()

file_result = str.join(",", headers) + "\n"

for row in json_result:
    for header in headers:
        # file_result += str(row[header]) + ","
        file_result += "\"" + str(row[header]) + "\","
    file_result += "\n"

json_write = open("dynamic_result.csv", "w")
json_write.write(file_result)
