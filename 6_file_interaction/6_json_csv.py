import json


json_file = open("randomNames.json", "r")

json_string = json_file.read()
output_list = json.loads(json_string)

csv_output_string = "First Name,Last Name\n"

for name in output_list:
    csv_output_string += name["first_name"] + "," + name["last_name"] + "\n"

csv_file = open("jsonCSV.csv", "w")

csv_file.write(csv_output_string)
