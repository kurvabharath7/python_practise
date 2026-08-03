import json
with open("nested_json","r")as file:
    data=json.load(file)
    print(data)

    print(data["employee"]["emp_name"])