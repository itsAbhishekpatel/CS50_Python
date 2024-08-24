"""
match case its like switch case 
"""

name = input("What's your name?")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")

# reduce the redundancy of the code 
# elif name == "Hermione":
#     print("Gryffindor")

# elif name == "Ron":
#     print("Gryffindor")

elif name == "Draco":
    print("Slytherin")
else :
    print("WHo?")


# use match 
match name:
    case "Harry" | "Hermione" | "Ron": # or = |
        print("Gryffindor")
    # case "Hermione":
    #     print("Gryffindor")
    # case "Ron":
    #     print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")