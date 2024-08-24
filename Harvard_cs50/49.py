# operator overloading(same name but different functionality) and 
# Operator Overriding(chnage the functinality)
# overloading occurs when methods in the same class have the same method name but different parameters,
# whereas overriding occurs when two methods have the same method name and parameters.
class Vault:
    def __init__(self,galleons = 0,sickles = 0,knuts = 0) -> None:
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    # by defualt str funcition call automatically when object is created and return
    # memory location of the object
    def __str__(self) -> str:
        return f"{self.galleons} {self.sickles}, {self.knuts}"
    
    # overloading + operator 
    # define add to add two object Vaults 
    def __add__(self,other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons,sickles,knuts)

    
potter = Vault(100,200,300)
print(potter)
# print(potter) priting the object give only memory location unit you overwite it 
# with dunder str function 
wasley = Vault(500,600,700)
print(wasley)

print(potter+wasley) #unsoptted operand, python does not know how to add, so lets teach the python
