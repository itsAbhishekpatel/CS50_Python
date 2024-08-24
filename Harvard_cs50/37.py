# read every line in the file
with open("name.txt","r") as file:
    for line in file:
        print(line.rstrip())

