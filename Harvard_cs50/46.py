import random
class Hat:

    # we do not intialise list every time the object is created 
    # intinalise a list 
    # def __init__(self) -> None:
    #     self.houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slutherin"]

    # so create class variable and its same for every object and created once
    houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slutherin"]
    #houses is a class variale, access by every method


    # def sort(self,name):
    #     house = random.choice(self.houses)
    #     print(f"{name} is in, {house}.")

    # use decorator to make any fucntion a class function 
    @classmethod
    def sort(cls,name):
        print(f"{name} is in, {random.choice(cls.houses)}")
        # cls means class variable 

    
# object hat from Hat class 
# do not instanciate any object to use class method 
# hat = Hat()

# use class name to use class methods 
Hat.sort("Abhishek") #calling class method
print(Hat.houses) #access class attributes 

# cls = refrenece of the class itself
# Use class when you have implment some real world entity  
# class is a blueprint which allow you to create one or more objects 
# classess is a way to modeling the world and solve the problem 
# OOps is all about Enscapalting data, functionlity or you can define your own modules, packages 