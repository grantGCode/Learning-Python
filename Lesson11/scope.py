# Understanding Scope applies to variables and functions.

name = "Grant" # Global Scope / available to everything in file.
count = 1

def greeting(firstname):
    color = "blue" # Color inside local scope of the function
    print(color)
    print(name)
    print(firstname)

greeting("John")

# Functions have access to the global scope and it's own local scope.

def greeting2(name):
    print(name) # Returns: John 
    # Because John was passed in as an argument of the param name on line 20

greeting2("John")


def another():
    greeting("Adam") 
    # You can call another function inside another function if the function called is defined in the global scope like greeting().


another()


def another2():
    color = "red" # Color is defined in the parent scope of anther2().
    # count = 2 # Line 39 would return 2 because here I created anther variable.

    # global count # Here I fixed the issue on line 33 by using the global key word to reference the global variable of count on line 4.
    
    global count
    count += 1
    # Here on lines 37 & 38 I can modify the global variable in the function first by referencing it then by modifying it on line 38.
    print(count) 
    
    def greeting3(name): 
        #  nested function of greeting3() is defined in the local scope of anther2() and is only available inside of another2().
        
        nonlocal color # nonlocal keyword lest my code now I will be using the local scope and will be using the parent scope for my variable color.
        color = "Orange"
        print(color)
        print(name)

    greeting3("Kate") # greeting3 can be called inside another2() local scope.

another2()

# Polluting the Global Scope: 
    # It's best practice to not pollute the global scope by adding anything to it that you really do not have to add to it. Especially when working on a team with multiple other developers.