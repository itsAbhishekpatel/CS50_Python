class Student:

    # init function which intialise properties of objects 
    def __init__(self,name_p,house_p):

       #""" define variable for object, self is a object which make 
        # variable name and house then assing the paramerts which pass during making of object"""
        # name and house is the variable name 

        #We Adding variables to objects aka instances varibles to objects  
        # what you have to do with name_p and house_p , you have to store 
        # in the current object with self keyword (you can call anything)
        # self is give you the access of curren objects 
        self.name = name_p
        self.house = house_p

def get_student():
    name = input("Name ")
    house = input("House: ")

    # Student is a Function same name as class ,
    # its is constructor - constructor call which make object 
    #just pass the parameters to the function that variables you have to intialise for the objects
    student1 = Student(name,house)

    return student1


# classes are just code but the object take space in the memory, some chunk of bytes 