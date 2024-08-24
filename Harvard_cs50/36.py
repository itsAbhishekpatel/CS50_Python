# you can use with keyword to open file and close simultaneously 
name = input("What's your name? ")

# file will automatically close after this scope 
with open("name.txt","a") as file:
    file.write(f"{name}\n")

# open the file in read mode and readline 
with open("name.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print(line,end="")
# how to read file 