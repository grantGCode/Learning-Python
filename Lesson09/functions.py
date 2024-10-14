# When naming function names need to be all lowercase with for multiple words  separated by underscores.
# No capital letters or - hyphen   

# Basic function syntax in python.
def hello_world():
    print("Hello world!")

hello_world()

# Basic function syntax with params an arguments in python.
def sum(num1, num2):
    if(type(num1) is not int or type(num2) is not int):
        return 
    # None (is a default value in python if you add an early return just like on line 13.)
    return num1 + num2

total = sum(2,3)
print(total)
print(sum("a",3))

