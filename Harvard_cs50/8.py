"""
Round function - round(number [, ndigits]) [] in documentation represent its optionnal 

"""

x,y = input("Enter two number: ").split(" ")

z = float(x) + float(y)
div = float(x) / float(y)
print(f"{z:,}") # format the number 
print(f"{z:.2f}") # round the number by 2 digit 

# round the number 
print(div)
print(round(div,2))