# nesting of loop to print pattern 
# use loop to iterate - run multiple time  
def print_column(height):
    print(height*"#\n",end="")
    # for _ in range(height):
    #     print("#")

def print_rows(rows):
    print("?"*rows)

print_column(4)
print_rows(4)