#static methods 

# inhertance - defince classess to inherit properties 

class Wizard():
    def __init__(self,name) -> None:
        if not name:
            raise ValueError("Missing Name.")
        self.name = name
        # self.house = house

#  Studnet can also a Wizard so use parent class functionality as well by Passing the class as a arugumnet    
class Student(Wizard):
    def __init__(self, name,house) -> None:
        # use super function to use parent class functionality
        # Student inherit and use all funcnality by calling the super classess 
        super().__init__(name)
        self.house = house

student = Student("Harry", "Gryffindor") 

print(student.name,student.house)

