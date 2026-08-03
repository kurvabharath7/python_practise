import json

with open("employee.json", "r") as file:
    data = json.load(file)

print(data)

print(data["emp_name"])