"""
Logic build and how to write code cleaverly
"""

def main():
    x = int(input("What's x? "))

    # calling the function which returns true or false 
    if is_even(x):
        print("Even")

    else:
        print("Odd")


def is_even(x):
    return x%2 == 0
    # return true if x % 2 == 0 else False

main()