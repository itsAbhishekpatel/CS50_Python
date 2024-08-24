names = []
# By defualt file is open in read mode if you do not specify
with open("name.txt") as file:
    for name in file:
        names.append(name)

# to sort the list and iterate at the same time 
for name in sorted(names):
    print(f"Hello, {name}.", end="")