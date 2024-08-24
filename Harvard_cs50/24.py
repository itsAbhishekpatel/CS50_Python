# create a loop to take int from user 
def get_int():
    while True:
        try:
            x = int(input("Enter any integer: "))
        except ValueError:
            # you can pass the error with handle it by pass keyword
            print("Please enter the integer value only.")
        else:
            # return is stronger than break it do two thing 
            # return and break the loop 
            return x
        # else block associate with the try block not with the except 
    

print(f"X is {get_int()}")
# rasie is also there

y = input("Enter: ")

if not type(y) is int:
  raise TypeError("Only integers are allowed")


# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.