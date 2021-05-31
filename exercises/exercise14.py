# ----- Exercise 14 -----
some_list = ['a','b','c','d','b','m','n','n']

duplicates = list(set([char for char in some_list if some_list.count(char) > 1])) 

print(duplicates) # ['n', 'b']