# Reclusion occurs when a function calls it's self.

def add_one(num):
    
    if(num >= 9):
        return num + 1
    
    total = num + 1
    print(total)

    return add_one(total)


# add_one(0) # Returns: 1 2 3 4 5 6 7 8 9

# Setting a new value
mynewtotal = add_one(0)
print(mynewtotal) # Returns: 1 2 3 4 5 6 7 8 9 None