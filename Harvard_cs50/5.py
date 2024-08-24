"""
 string - sequnece of character
 inbuilt function for string like strip(), split(), capitalize() etc.
 These are Methods of string which is predefined into python already.
"""

name = " abhishek, Patel  "
# remove space from start and end 
name = name.strip().title().lower() # return a string without any space at left or right

name = name.capitalize() # return a string with first captial letter

f,l = name.split(",") # split the string into sub string by , you can split by space also

print(name)
print(f,l)