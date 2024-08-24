# go and read documnentation for this library 
# re.search(pattern,string,flag=0)
# regex = regular expression library 
import re

# symbol in regular expression 
""". any character expect a new line 
* 0 or more repetation
+ 1 or more repetation
? 0 or 1 repetation
{m} m repetations
{m,n} m-n repetation

^ match the start of the string
$ match the end of the string or just before the new lineat the end of the string 

[] set of characters
[^] complementing the set
"""

email = input("What's your email?").strip()

# using search function of regex library
# make the string a raw string - pass exactly it is 
# make raw sting for regular expression
# regular exp use every where to find patterns or valid something
if re.search(r"^[^@]+@[^@]+\.edu$",email): 
    print("Valid")
else:
    print("Invalid")