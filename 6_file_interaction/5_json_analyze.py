import json


json_file = open("randomNames.json", "r")

json_string = json_file.read()
output_list = json.loads(json_string)

last_name_analysis = {}
first_name_analysis = {}

for name in output_list:
    if name["first_name"] in first_name_analysis.keys():
        first_name_analysis[name["first_name"]] += 1
    else:
        first_name_analysis[name["first_name"]] = 1

    if name["last_name"] in last_name_analysis.keys():
        last_name_analysis[name["last_name"]] += 1
    else:
        last_name_analysis[name["last_name"]] = 1

print(last_name_analysis)
print(first_name_analysis)
