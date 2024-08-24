"""
Create list of dictionary 
"""

# a collection of values - dic 
student = [
    {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
    {"name":"Draco","house":"Slytherin","patronus":None},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
]

# So you can print name of the all students 
for student in student:
    print(student["name"],student["house"],student["patronus"], sep= " , ")