# ----- Exercise 13 -----

# square
my_list = [5,4,3]

print(list(map(lambda num: num ** 2, my_list))) # [25, 16, 9]

# list sorting - sort 2nd item
a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key=lambda item: item[1])
print(a)