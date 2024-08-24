"""
Making your own function - define and use them 
use () to call any function like print or input 
use def keyword to define any function
You should always define the function at top of the program so it already exit before callig it
"""

# defining the function with one parameter and have default value world
def hello (to = "World"):
    """Take's user name and say Hello""" # docs string which tell about the function
    print(f"Hello, {to}")

# calling the function and passing one arugment which needed 
name = input("What's your name? ")
hello(name) 
hello() # call the fucntion with default value 

