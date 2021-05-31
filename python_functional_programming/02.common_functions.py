# ----- Map -----
my_list = [1,2,3]

def multiply_by2(num):
  return num * 2

print(list(map(multiply_by2, my_list))) # [2,4,6]

# ----- Filter -----
def only_odd(num):
  return num % 2 != 0

print(list(filter(only_odd, my_list))) # [1,3]

# ----- Zip -----
your_list = [10,20,30]
their_list = [100,200,300]

# zip items into tuple
print(list(zip(my_list, your_list))) # [(1, 10), (2, 20), (3, 30)]
print(list(zip(my_list, your_list, their_list))) # [(1, 10, 100), (2, 20, 200), (3, 30, 300)]

# ----- Reduce -----
from functools import reduce

def accumulator(acc, item):
  print(acc, item)
  return acc + item

print(reduce(accumulator, my_list, 0)) # 6