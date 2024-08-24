# Exceptions in python, how to handle it
# try to write the code use expect to handle it 
# ValueError to handle the error 
# write those code in try which case error and print does not make error
# There is many types of error ValueError, NameError etc
try:
    x = int(input("Enter any interger number: "))
except ValueError:
    print("X is not an interger")
else:
    print(f"X is {x}")

# when the try block run so excpetion block no need to run
# and else statment will be executed
