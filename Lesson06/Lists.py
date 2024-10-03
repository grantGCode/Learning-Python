users = ['Grant', 'Dave', 'John'] # Basic list with String.

data = ['Grant', 28, True] # List with String, Number, and Bool.

empty = [] # Empty list.

print('Grant' in empty) # Return True or false if data is present.

print(users[0]) #return Grant
print(users[-2]) #return Dave

print(users.index('John'))

print(users[0:2]) # Return [Grant, Dave]
print(users[1:]) # Return [Dave, John]
print(users[-3:-1]) # Return [Grant, Dave]

print(len(data)) # Returns length of the data list: 3

users.append('Fido')
print(users)
# print('users list has ', + str(len(users)), + " values.")