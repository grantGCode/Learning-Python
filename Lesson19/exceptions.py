# Python exceptions
class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom Exception!")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.") 
        # raise one of the built in Python error with the raise statement.
except NameError: 
    # just add except: will catch all errors.
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error: 
    # This will catch the raised TypeError Exception on line 7.
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error.")