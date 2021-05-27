# lists that are immutable
# faster performance than list because less flexible

my_tuple = (1,2,3,4,5)

print(my_tuple[1]) # 2
print(5 in my_tuple) # True

new_tuple = my_tuple[1:2]

print(new_tuple) # (2,)

x,y,z, *other = (6,7,8,9,10)

print(x) # 6
print(other) # [9, 10]

# ----- Tuple built-in functions & methods -----

# count
print(my_tuple.count(5)) # 1

# index
print(my_tuple.index(5)) # 4

# len
print(len(my_tuple)) # 5