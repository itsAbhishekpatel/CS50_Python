"""
Dictionary - store info in key value pair
delcare with { } or use dict constructor

"""

# declare dic 
students = {
    "Hermione":"Gryffendor",
    "Harry":"Gryffendor",
    "Ron":"Gryffendor",
    "Draco":"Slytherin"
}

# access values by keys 
print(students["Hermione"])

# When you use for loop to iterate over a dictionary it goes through keys 
for keys in students:
    print(keys, students[keys], sep= " - ")
