# there are third party libraries know as packages 
"""so you can install packages in you system and gain more fucntionality which is Implemented
by other people """

# pypi.org is a website where you search python packages 

"""pip is the package manager - pip is a program which comes with python which allow 
you to install packages"""

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, "+sys.argv[1])
    cowsay.trex("hello")

# ASCII art - print something 