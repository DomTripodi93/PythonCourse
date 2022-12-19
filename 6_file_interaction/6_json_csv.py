import json

json_file = open("random_names.json")

json_test_string = json_file.read()

json_result = json.loads(json_test_string)


file_result = "first_name,last_name\n"

for name in json_result:
    # print(name)
    file_result += name["first_name"] + "," + name["last_name"] + "\n"

json_write = open("random_names_spreadsheet.csv", "w")
json_write.write(file_result)
