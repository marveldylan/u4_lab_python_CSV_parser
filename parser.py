####################################################
#  python library imports here: csv, json
import csv
import json

####################################################
# Set up 3 global variables to process the csv file 
# and convert it to JSON
# All variables will be empty lists to start: []
read_data = []
fields = []
employee_list = []

####################################################
# main function 
# Takes in the path of the csv file and an output path 
# for creating a new JSON file as arguments
# creates a new JSON file with formatted csv data
def csv_to_json(csv_path, json_path):
    with open(csv_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for row in csv_data:
            read_data.append(tuple(row))
    headers = read_data[0]
    employees = read_data[1:]
    for i, field in enumerate(headers):
        name = field.lower().replace(' ', '_')
        fields.append(name)
    for i, employee in enumerate(employees):
        new_dict = {}
        for i, entry in enumerate(employee):
             new_dict[fields[i]] = entry
        employee_list.append(new_dict)
        new_dict = {}
    with open(json_path, mode='w') as output_file:
        json.dump(employee_list, output_file, indent=2)
csv_to_json('data/employee_data.csv', 'data/employees.json')
