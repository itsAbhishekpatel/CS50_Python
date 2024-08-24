# printing pattern - 2 dimensinal 

def print_square(size):
    # for each row in square 
    for i in range(size):
        # for each brick in square 
        for j in range(size):
            print(".  ",end="")
        print()

print_square(5)