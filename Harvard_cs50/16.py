"""
Loops use to do repeative task - for, while loop and we can nested it as well

"""

# you have to update the condition to end the loop
i = 3
while i != 0:
    print("meow")
    i -= 1

name = ["Abhishek","John","Grany"]

#using the for loop to iterate in list
for stu in name:
    print(stu)

# using range funciton with for loop 
for i in range (10):
    print(i, end= " ")
