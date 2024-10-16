# modules are considered small code library's basie on related features.

#Built in Modules from Python
import math 
# Alow you to use mathematical tasks.

import sys 
# Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

import random as rdm 
# Implements pseudo-random number generators for various distributions.


# Custom modules

import texas 
from rps7 import rock_paper_scissors

print(math.pi) 

# using dot notation to pull a value or function from the module.

from enum import Enum # or import a  value or function from the module.

# enum is a value from the Enum Module

# rdm.choice('123') 

# Using an alias to use random module.
# Alias created on line 10 with the "as" syntax. 


# for item in dir(rdm):
#     print(item)

#the dir() function will show you a directory of value and function available to use in a module.
# The for loop makes the directory look more legible in the terminal.

print(texas.capital) 
# Print the capital value from the texas.py custom module.

texas.randomfunfact() 
# Using the randomfunfact() function in the texas.py custom module.

# The __name__ value
# Is a special value every module has

print(__name__) # Returns: __Main__ 
# Main is the name of the current module being ran / you are using.

print(texas.__name__) # Returns: texas

rock_paper_scissors() # Will start Rock paper scissors game when file is ran.


# More on the Python Module Index here:
    # https://docs.python.org/3/py-modindex.html
