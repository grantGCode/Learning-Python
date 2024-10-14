# How while loops evaluate the True or False condition.

# Example 1
value = True

# I could put: while value == True But syntax of line 7 implies value is True.
while value: # Wile value is True
    print(value)
    value = False # or 0 which = False
    # On line 8 value is now false loop will check if value is true then exit.

# Example 2
value = "y" # or value exists which = True
count = 0


while value: 
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue # Loop will check the value on line 6 if loop should execute.