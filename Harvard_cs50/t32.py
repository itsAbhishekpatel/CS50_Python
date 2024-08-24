# unit test - test the code by passing some sample input 
# testing your own code by using code of your own
# write the code to test your code which you wrote 
def main():
    x = int(input("What's x? "))
    print("x square is,",square(x))

def square(x):
    return x*x

# main is always call wiht name and main 
"""I am doing this becasue when i import this module 
so by default main function is not get called by itslef"""
if __name__ == "__main__":
    main()

# write a different program which has a prupose to test this program  
