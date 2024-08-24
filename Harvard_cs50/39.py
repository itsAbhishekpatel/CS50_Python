# Regular Expression - find out pattern in our data 
# Lets solve some probelem with regular expression 
email = input("What's your emial?").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

# It is not a good approach, so we use regular expression and use library - re 