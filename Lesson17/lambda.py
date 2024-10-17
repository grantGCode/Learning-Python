# Lambda functions:
    # A Lambda function is a single expression that returns a function.
    # return statements are not needed.
    # Lambda functions are considered anonymous functions.
    # Lambda functions can be assigned to a value.

squared = lambda num : num * num

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))

# Lambda Expressions can also accept 2 parameters as seen below.
sum_total = lambda a, b : a + b

print(sum_total(10, 8))

#############################

# When to Use Lambdas:
    # Most often nested inside another function
    # Functions you don't want to save for later.

def funcBuilder(x):
    return lambda num : num + x # Retuning a lambda function

add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))
print(add_twenty(7))

#############################

# High order functions
    # High order functions are a function that takes in one or more functions as arguments or returns a one or more functions as a result. (Kind of like Line 25)

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

#############################

odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

#############################

from functools import reduce

numbers = [1, 2, 3, 4, 5, 1]

# total = reduce(lambda acc, curr : acc + curr, numbers) 
total = reduce(lambda acc, curr : acc + curr, numbers, 10) 
# Telling reduce() to start with 10

print(total)

# print(sum(numbers)) 
print(sum(numbers, 10)) 
# Simpler solution use the built in sum() function than using reduce

#############################

names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)
# Putting a starting value of 0 to tell reduce() that I going to strings than numbers.

print("Character count = ",char_count)