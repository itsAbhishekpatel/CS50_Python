# importing the sys module 
import sys

if len(sys.argv) < 2:
    # exit from the program 
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
name = []
for arg in sys.argv:
    name.append(arg)

print("Hello, ",sys.argv[1])
print(name)

