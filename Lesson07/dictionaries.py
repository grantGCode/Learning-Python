#Python Dictionaries

# Dictionaries are data values that store key value pairs 
# just like JavaScript Objects.

band = {
    "vocals": "Plant",
    "guitar": "Page",
}

band2 = dict(vocals ="Plant", guitar="Page")
# dict is the dictionary constructor.

print(band)
print(band2)
print(type(band))
print(type(band2))
print(len(band))
print(len(band2))

# Access items in a Dictionary
print(band["vocals"]) # Using []
print(band.get("guitar")) # Using .get

# List all keys
print(band.keys())

#List all values
print(band.values())

#List of key/value pairs as tuples
print(band.items())

# Verify if a key exists
print("guitar" in band) # Returns: True
print("triangle" in band) # Returns: False

# Changing values
band["vocals"] = "Coverdale" # Specifying Key in []. 
# Will set Plant to Coverdale in band.
band.update({"base": "JPJ"}) # Change or add new key/value pair.

print(band)

# Remove items
print(band.pop("base")) 
# pop() will return the value what I removed Not the key.
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) 
# popitem() pop off the last list item 
# and will return the full key/value pair I popped as a tuple.
print(band)

# Delete or clear item
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear() # clear() will empty out the dictionary.
print(band2) # Returns: {}

del band2 # No output after I delete the band2 dictionary.

# Copy Dictionary

# How not to create a copy
# band2 = band # Not a real copy this creates a reference
# print(band2, 'Bad copy!')
# print(band)

# band2["drums"] = "Dave"
# print(band) # Will return the drums key/value pair that I added to band2 ref.

# How to actually create a copy.
band2 = band.copy()
band2["drums"] = "Dave"
print(band) # Returns: {'vocals': 'Coverdale', 'guitar': 'Page'}
print(band2, "Good copy!") # Returns: {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'} Good copy!

# or use the dict() constructor function
band3 = dict(band)
print(band3, "Good copy!")
# Returns: {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'} Good copy!

# Nested Dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"]) # band[1 level deep][2 levels deep]

# Sets

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
print(nums) # Returns:
