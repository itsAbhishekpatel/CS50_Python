
class Student:

    def __init__(self,name,house) -> None:

        # raise the error when the object does not get desire object 
        # you can handle this error as well by try and except 
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Huffelepuff","Ravenclaw","Slytherin" ]:
            raise ValueError("Invalid House")
        self.name = name 
        self.house = house

    # also a dunder function 
    #only take one argument 
    # self is a refrence of object which try to printed
    # it call automatically when object is try to print
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
        

stu = Student(input("Name:"), input("House:"))

# print(f"{stu.name} from {stu.house}")

"""dunder str function is call which overwrite the location value of object 
and return whatever string you want"""
print(stu)

# So there is __str__ is automatically called when someone see your object as a string 
# you can create your own library 