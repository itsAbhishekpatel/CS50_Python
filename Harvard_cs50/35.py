# File I/O 
names = []

# open the file and if file is not exit it will created
# file = open("name.txt","w") w will overwite the file so use append which add data in the bottom
file = open("name.txt","a")

for _ in range(3):
    name = input("What is your name? ")
    file.write(f"{name}\n")

# print(file.read())

file.close()

# print(f"hello, {names}")