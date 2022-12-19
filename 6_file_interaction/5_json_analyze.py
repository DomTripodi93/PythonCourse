import json

json_file = open("random_names.json")

json_test_string = json_file.read()

json_result = json.loads(json_test_string)

first_name_analysis = {}
last_name_analysis = {}

for name in json_result:
    # print(name)
    if name["first_name"] in first_name_analysis.keys():
        first_name_analysis[name["first_name"]] += 1
    else:
        first_name_analysis[name["first_name"]] = 1

    if name["last_name"] in last_name_analysis.keys():
        last_name_analysis[name["last_name"]] += 1
    else:
        last_name_analysis[name["last_name"]] = 1

print(first_name_analysis)
print(last_name_analysis)
