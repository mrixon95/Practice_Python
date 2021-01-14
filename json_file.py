import json
# lets read the JSON object from a file
# we can conver the JSON object to a python object using the dump method
with open("data_file.json") as JSON_object_from_file:
    python_object = json.load(JSON_object_from_file)

print(python_object)