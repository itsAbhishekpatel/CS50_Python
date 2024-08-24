"""Create your own data type as well, make class = a bluprint  
create your own objects 
1. classes have attributes-varibales (proerties of objects) to store data
2. classes have methods-functions (functionality of object) to perform something
3. Whenever you have to use class, you have to create objects
"""

class Student:
    ...

def main():
    Student = get_student()
    print(f"{Student.name} from {Student.house}")

def get_student():
    # Create an object of Student Class 
    student = Student()

    #create varibales of student object which is created above 
    student.name = input("Name: ")
    student.house = input("House: ") 

    # return the object
    return student #own data type, an object 

if __name__ == "__main__":
    main()

# __ is called duner means dunder functions 

# use dunder init fucntion to intialise things for objects