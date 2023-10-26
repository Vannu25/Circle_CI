student = {
    "name": "Emma",
    "class": 9,
    "marks": 75
}

m = student.get('marks')
print(m)

dict1 = {"name": "Mike", "salary": 8000}
# temp = dict1.pop("age") - key error
# print(temp)


student = {
    "name": "Emma",
    "class": 9,
    "marks": 75
}
#
# student.pop("marks")
# print(student)

# del student["marks"]
# student.popitem()  # last item


# student.remove("marks")  # remove object is not available.
print(student)

dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)

student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}

s = student[1]["age"]
print(s)
# s1 = student[0]["age"] - key error
# print(s1)

sampleDict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}

m = sampleDict['class']['student']['marks']['history']
print(m)

sampleDict = dict([('first', 1), ('second', 2), ('third', 3)])
print(sampleDict)
