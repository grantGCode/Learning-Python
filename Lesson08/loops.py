# While loop

value = 1
# while value <= 10:
#     print(value)
#     value += 1

# While loop with break statement.
# Loop will stop at 5.

# while value <= 10:
#     print(value)
#     if value == 5: 
#         break
#     value += 1

# continue statement will go to the next iteration of the loop when it gets to 5.

# while value <= 10:
#     value += 1
#     if value == 5: 
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))


# For loops


names = ["Grant", "Kate", "Adam"]
# for x in names:
#     print(x) # Returns: Grant Kate Adam

# for x in "Mississippi":
#     print(x) # Returns: M i s s i s s i p p i 

# for x in names:
#     if x == "Kate":
#         break # Iteration: ["Grant", "Kate"]
#     print(x)

# for x in names:
#     if x == "Kate":
#         continue # Iteration: ["Grant", skip, "Adam"]
#     print(x)

# for x in range(4): # range(Stop)
#     print(x) # Returns: 0 1 2 3

# for x in range(2, 4): # range(Start, Stop)
#     print(x) # Return: 2 3 

# for x in range(5, 101, 5): # range(Start, Stop, but_increment_by)
#     print(x) 
# else:
#     print('Glad that\'s over!')

# Nested loops
names = ["Grant", "Kate", "Adam"]
actions = ["codes", "studies", "works"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")