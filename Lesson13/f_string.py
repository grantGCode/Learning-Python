person = "Grant"
coins = 3

#################
# Concatenating strings

print("\n" + person + " has " + str(coins) + " coins left.")

# old ways to use strings before f_strings

# %s method
message = "\n%s has %s coins left." % (person, coins)
# %s inserts the first param where the first instance of %s is int he string.
print(message)

# .format method
message = "\n{} has {} coins left.".format(person, coins)
print(message)
# or 
message = "\n{1} has {0} coins left.".format(coins, person)
print(message)
# or
message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person)
print(message)


# Dictionary method

player = { 'person': 'Grant', 'coins': 3 }

message = "\n{person} has {coins} coins left.".format(**player)
print(message)


##################
# modern f-Strings!

message = f"\n{person} has {coins} coins left."
print(message)
# or
message = f"\n{person} has {2 * 5} coins left."
print(message)
#or I can use/pass in methods
message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)
# using the dictionary on line 30
message = f"\n{player['person']} has {2 * 5} coins left."
# Take note what quotes ("", '') your using because using the same quotes inside the [] will cause an error.
print(message)


##################
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n") # 2f adds decimal points.

# adding or using loops
for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}\n")


for num in range(1,11):
    print(f"{num} divided by 4.52 {num / 4.52:.2%}\n") 
    # 2% adds decimal points and a %.

# Helpful link for more Python formatting method() types:
    #  https://www.w3schools.com/python/ref_string_format.asp