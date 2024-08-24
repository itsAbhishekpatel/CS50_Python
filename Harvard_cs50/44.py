
class Student:

    def __init__(self,name,house,patronous) -> None:

        # raise the error when the object does not get desire object 
        # you can handle this error as well by try and except 
        if not name:
            raise ValueError("Missing Name")
        # if house not in ["Gryffindor", "Huffelepuff","Ravenclaw","Slytherin" ]:
        #     raise ValueError("Invalid House")
        self.name = name 
        self.house = house
        self.patronous = patronous

    # also a dunder function 
    #only take one argument 
    # self is a refrence of object which try to printed
    # it call automatically when object is try to print
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    # it is function inside a class so it take atleast one argument which is self
    # so that you have to access of the current object
    def charm(self):
        match self.patronous:
            case "Stag":
                return "🏰🧙‍♂️🪄🦁"
            case "Otter":
                return "👽🐍🪄"
            case _:
                return "Sorry! nothing is there for you."
    #Getter - a function for a class that get some attribute
    # for getter use @property decortor
    @property
    def house1(self):
        return self.house1
    #Setter - a function for a class that sets some attributes 
    # when house variable is created automatically setter function is call 
    # does not acess the variable direclty, use getter 
    # for setter use @house.setter
    @house1.setter
    def house1(self,house):
        if house not in ["Gryffindor", "Huffelepuff","Ravenclaw","Slytherin" ]:
            raise ValueError("Invalid House") 
        self.house1 = house


stu = Student(input("Name:"), input("House:"), input("Patronous:"))

# print(f"{stu.name} from {stu.house}")

"""dunder str function is call which overwrite the location value of object 
and return whatever string you want"""
print(stu)
# stu.house1 = input("house")
print(f"Expecto Patrono! {stu.charm()}")

# So there is __str__ is automatically called when someone see your object as a string 
# you can create your own library 

# there are many other methods which comes with python classess 
# functions inside a class aka method 

# decorators = functions which modify the behavior of other functions 
# use getter and setter to not change blindly assign the value of the varibale 