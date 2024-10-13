# Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are used to store multiple items in a single variable.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Sets are written with {} brackets.

nums = {1, 2, 3, 4} # Creating a set

nums2 = set((1, 2, 3, 4)) # Creating a set with the set constructor 

print(nums)
print(nums2)
print(type(nums)) # Returns: <class 'set'>
print(len(nums)) # Returns: 4

# No duplicate are allowed in a set see example below.
nums = {1, 2, 2, 3}
print(nums) # Returns: {1, 2, 3}

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums) # Returns: {False, 1, 2, 3, 4}
# 1 and 0 are considered True and False in code.

# checking if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# With update() you can also pass in list, tuples, and dictionaries, too.

# Merge 2 sets to create a new set.
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one) # Returns: {2, 3}

# This changes one and will only keep the duplicate values

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one) # Returns: {1, 4}