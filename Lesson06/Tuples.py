# Tuples 
# A tuple is a collection which is ordered and unchangeable.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuples use the () than [] for lists

# Tuples are like lists but are different, the data inside tuples will not change and the order the data is in will not change.

mytuple = tuple(('Grant', 28, True)) # Creating tuple with the tuple constructor.

anothertuple = (1,4,2,8) # Creating a tuple with out a constructor.

print(type(mytuple)) # Returns: <class 'tuple'>
print(type(anothertuple)) # Returns: <class 'tuple'>

# If I do need to change the content of a tuple or "Pack the tuple." The best way to go about that is to copy the tuple to a new list the create a new tuple by copying that list you just created.

newlist = list(mytuple) # Copy tuple to a list.
newlist.append('Neil') # Append the new value to the newlist.
newtuple = tuple(newlist) # Then I can make a new tuple out of the content of newlist.
print(newtuple) # Returns: ('Grant', 28, True, 'Neil')

# Unpacking a tuple

(one, two, *hey) = anothertuple # See line 129 for anothertuple
print(one) # Returns: 1
print(two) # Returns: 4
print(hey) # Returns: [2, 8]

# or

# (one, *two, hey) = anothertuple # See line 129 for anothertuple
# print(one) # Returns: 1
# print(two) # Returns: [4, 2]
# print(hey) # Returns: 8

# The * next to the tuple value will retune the remaining values in the tuple in to a list as seen above.

counttuple = (1,4,2,8,2,2)
print(counttuple.count(2)) # Returns: 3
# count will show how may occurrences of a value are in the tuple or list.
