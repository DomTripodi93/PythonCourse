import json


json_file = open("dynamicJSON.json", "r")

json_string = json_file.read()
output_list = json.loads(json_string)

headers = dict(output_list[0]).keys()

csv_output_string = str.join(",", headers) + "\n"

for row in output_list:
    output_row = ""
    for header in headers:
        # output_row += str(row[header]) + ","
        output_row += "\"" + str(row[header]) + "\","
    csv_output_string += output_row + "\n"

csv_file = open("dynamicCSVOutput.csv", "w")

csv_file.write(csv_output_string)
