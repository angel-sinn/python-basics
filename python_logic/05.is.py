# is vs ==

print(True == 1) # True
print('1' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True
print([1,2,3] == [1,2,3]) # True

# == checks for equality of value

print(True is True) # True
print('1' is '1') # True
print([] is []) # False
print(10 is 10) # True
print([] is []) # False
print([1,2,3] is [1,2,3]) # False

# is checks if location in memory is same
# data structures are always created in new location