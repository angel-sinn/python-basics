# unordered collections of unique objects

my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(2)

print(my_set) # {1,2,3,4,5, 100}

# convert list to set
my_list = [1,2,3,4,5,5]

print(set(my_list)) # {1, 2, 3, 4, 5}

# convert set to list
new_set = my_set.copy()

print(list(new_set)) # [1, 2, 3, 4, 5, 100]

# 'in' - does something exist
print(1 in my_set) # True

# length
print(len(my_set)) # 6 - doesn't include duplicates

# clear
my_set.clear()
print(new_set) # {1, 2, 3, 4, 5, 100}
print(my_set) # set()

# ----- Set built-in functions & methods -----
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

# difference
print(set1.difference(set2)) # {1, 2, 3}

# discard
print(set1.discard(5)) # None
print(set1) # {1, 2, 3, 4}

# difference_update
print(set1.difference_update(set2)) # None
print(set1) # {1, 2, 3}

# intersection
set1 = {1,2,3,4,5}

print(set1.intersection(set2)) # {4, 5}
print(set1 & set2) # {4, 5}

# disjoint - has nothing in common
print(set1.isdisjoint(set2)) # False

# union - removed duplications
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# subset - inside the second set?
set1 = {4, 5}

print(set1.issubset(set2)) # True

# superset - does first set include second set?
set1 = {4, 5}

print(set1.issuperset(set2)) # False
print(set2.issuperset(set1)) # True