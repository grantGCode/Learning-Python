# Lists
# List items are ordered, changeable, and allow duplicate values.

users = ['Grant', 'Dave', 'John'] # Basic list with String.

data = ['Grant', 28, True] # List with String, Number, and Bool.

empty = [] # Empty list.

print('Grant' in empty) # Return True or false if data is present.

print(users[0]) # Returns: Grant
print(users[-2]) # Returns: Dave

print(users.index('John'))

print(users[0:2]) # Return [Grant, Dave]
print(users[1:]) # Return [Dave, John]
print(users[-3:-1]) # Return [Grant, Dave]

print(len(data)) # Returns: length of the data list: 3

#Adding items to lists 

users.append('Fido')
print(users)

users += ['Jason'] # Adding another list to my already existing list.
print(users) # Returns: ['Grant', 'Dave', 'John', 'Fido', 'Jason']

# Note: When adding a list and to another using += make sure the string is wrapped in [] or else it will add ever letter in the string as a key value.

# users += 'Jason'
# print(users) # Returns: ['Grant', 'Dave', 'John', 'Fido', 'Jason', 'J', 'a', 's', 'o', 'n']

users.extend(['Kate', 'Adam']) # Adding a list to my current list with extend()
print(users) # Returns: ['Grant', 'Dave', 'John', 'Fido', 'Jason', 'Kate', 'Adam']

# users.extend(data) 
# #Passing in a pre-existing list to my users list. 
# print(users) # Returns: ['Grant', 'Dave', 'John', 'Fido', 'Jason', 'Kate', 'Adam', 'Grant', 28, True]

#Picking an index/spot to add new list data to existing list

users.insert(0, 'Bryan') 
# Adding Bryan at index 0 of the users list using inserts()
print(users) # Returns: ['Bryan', 'Grant', 'Dave', 'John', 'Fido', 'Jason', 'Kate', 'Adam']

users[2:2] = ['Michele', 'Pamela'] 
# Using bracket notation to insert at the position NOT replace.
print(users) # Returns: ['Bryan', 'Grant', 'Michele', 'Pamela', 'Dave', 'John', 'Fido', 'Jason', 'Kate', 'Adam']

users[1:3] = ['Robert', 'JPJ'] 
# Replacing users at a index/position position also referred to as a slice.
print(users) # Returns: ['Bryan', 'Robert', 'JPJ', 'Pamela', 'Dave', 'John', 'Fido', 'Jason', 'Kate', 'Adam']

#Removing data from list

users.remove('Robert')
# Removing user from list using remove()
print(users) # Returns: ['Bryan', 'JPJ', 'Pamela', 'Dave', 'John', 'Fido', 'Jason', 'Kate', 'Adam']

# pops of last user but does not change list using pop().
print(users.pop()) # Returns: ['Bryan', 'JPJ', 'Pamela', 'Dave', 'John', 'Fido', 'Jason', 'Kate', 'Adam']  Adam
print(users) # Now Returns: ['Bryan', 'JPJ', 'Pamela', 'Dave', 'John', 'Fido', 'Jason', 'Kate']

del users[1] # deletes user from list using del.
print(users) # Returns: ['Bryan', 'Pamela', 'Dave', 'John', 'Fido', 'Jason', 'Kate']

# del data # Deleting an entire list using del.
# print(data) # Returns: NameError: name 'data' is not defined

data.clear() # Clearing all data from a list using clear(). 
print(data) # Returns: []

# Sorting data in a list

# Note: The Sort Method does modify the list.

users.sort() # Sorts list in alphabetical order.
print(users) # Returns: ['Bryan', 'Dave', 'Fido', 'Jason', 'John', 'Kate', 'Pamela']

# sort() is case sensitive watch as I replace and add 'grant' to the list and sort() afterword.
users[2:3] = ['grant']
users.sort() 
print(users) # Returns: ['Bryan', 'Dave', 'Jason', 'John', 'Kate', 'Pamela', 'grant']

users.sort(key=str.lower) # passing in key=str.lower the sort() bypasses the methods case sensitivity.
print(users) # Returns: ['Bryan', 'Dave', 'grant', 'Jason', 'John', 'Kate', 'Pamela']

nums = [4, 42, 78, 1, 5]
nums.reverse() # revers() reveres the index order of a list note the data inside the list.
print(nums) # Returns: [5, 1, 78, 42, 4]

# nums.sort(reverse=True) # Returns the list with the data sorted in descending order.
# print(nums) # Returns: 

# using the sorted() function will not modify the nums list whin I print it again.
print(sorted(nums, reverse=True)) # Return:  [78, 42, 5, 4, 1]
print(nums) # Returns: [5, 1, 78, 42, 4]

#Making copies of lists

numscopy = nums.copy() # Creates a copy of nums
mynums = list(nums) # Creates a copy of nums using the list() constructor.
mycopy = nums[:] # Will splice nums and add all the data of numbs to mycopy list as a copy of nums. 
print(numscopy) # Returns: [5, 1, 78, 42, 4]
print(mynums) # Returns: [5, 1, 78, 42, 4]
print(mycopy) # Returns: [5, 1, 78, 42, 4]
print(nums) # Returns: [5, 1, 78, 42, 4]
# All 4 look the same but are not the same top 3 are copies of nums.

mycopy.sort() # Here I am sorting mycopy just following along.
print(mycopy) # Returns: [1, 4, 5, 42, 78]

# Displaying list types

print(type(nums)) # Returns: <class 'list'>

# crating list with constructor

mylist =list([1, "Neil", True])
print(mylist)




