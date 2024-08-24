# OOps - Object Oriented Programming 
# When we write code its procedural in nature/ functional Programming
# and there is Object Oriented programming 

def main():
    name = get_name() #Abstarction - not know about the implementation
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("What's your name?")

def get_house():
    return input("What's your house name?")

# return multiple values by , - retrun tuple and do indexing and varible can't change
# you can return dictionay or list as well 
"""return {"name":name, "house":house}"""
# code run from here
if __name__ == "__main__":
    main()

# the above program is functional programming or Procedural Programming 
"""But What if student is something which call function for me """
# sequence data type = list and tuple 
# Key, values paired data tupe = Dictionary 
# Sets is another sequnece data type
