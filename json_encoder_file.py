import json
from json import JSONEncoder

class Student:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        
# JSONEncoder
class StudentEncoder(JSONEncoder):
    def default(self, o):
        dictionary = o.__dict__
        dictionary["__student__"] = True
        return dictionary

student = Student("Michael", 25, "Melbourne")

print("Encode Employee Object into JSON formatted Data using custom JSONEncoder")
studentJSONData = json.dumps(student, cls=StudentEncoder)

# The Student object encoded into JSON formatted Data String looks like this
print(type(studentJSONData)) # Output: <class 'str'>
print(studentJSONData) # Output: {"name": "Michael", "age": 25, "location": "Melbourne"}

# Likewise we can decode the JSON formatted Data back into a student object
# student_object = json.loads(studentJSONData, cls=StudentEncoder)
# print(type(student_object))
# print(student_object)


def decode_student(dct):
    if "__student__" in dct:
        return Student(dct["name"], dct["age"], dct["location"])
    return dct


student_object = json.loads(studentJSONData, object_hook=decode_student)

print(f"Type of student object: {type(student_object)}")
print(f"Name: {student_object.name}")
print(f"Age: {student_object.age}")
print(f"Location: {student_object.location}")