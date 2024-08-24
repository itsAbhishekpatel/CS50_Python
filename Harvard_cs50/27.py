# Sys library - use for interact with system 
import sys
# sys.argv[0] is the name of the program/ location
try:
    print("hello, my name is,",sys.argv[1]) 
# Basically in except we are overwriting the indexerror which will come 
except IndexError:
    print("Too Few Argumnets")
""" if you run the program it give error becuase at location 1 there is nothing """
