# When naming function names need to be all lowercase with for multiple words  separated by underscores.
# No capital letters or - hyphen   

# Basic function syntax in python.
def hello_world():
    print("Hello world!")

hello_world()

# Basic function syntax with params an arguments in python.
# The syntax of function(param=value) is setting a default value on line 12
# None (is a default value in python if you add an early return just like on line 17. 
# I can also have the code return a None value by setting the return statement to 0 as seen on line 18. That will retune a None value and is better than returning an unexpected statement like on line 17.

def sum(num1=0, num2=0): 
    if(type(num1) is not int or type(num2) is not int):
        # return # Returns: None
        return 0 # Returns: None
    return num1 + num2

total = sum(2,3)
print(total)
print(sum("a",3))

# print(sum()) Returns: TypeError: sum() missing 2 required positional arguments: 'num1' and 'num2'


# Functions with multiple unspecified prams.

# the args syntax is used to specify a given param even tho the syntax uses the word args it is in fact a parameter.
# The * syntax in front of the args sets the value to a tuple.

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Grant", "Kate", "Adam")

# Functions with multiple keyword arguments.
# The kwargs syntax  stands for (Multiple, Keyword, Arguments)
# The ** syntax in front of the kwargs sets the value to a dictionary.
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first='John', last="Doe")
