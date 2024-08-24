# module = already code written by some other developer 
# import the module and use it 

"""import random = importing everthing in the module 
   module_name.function_name"""
from random import choice, randint, shuffle

flip_coin = choice(["Head","Tail"]) # call the choice fucntion and pass a sequnece 
rand_num = randint(1,10)
x = [1,2,3,4,5]
shuffle(x)
print(f"{flip_coin} comes.")
print(f"{rand_num} is generated numder")
print(x)

"""when you are importing any library hope you do not use same name of function 
which is already exit it that"""