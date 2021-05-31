# generate sequence of values over time (range)

range(100) # creates one by one
list(range(100)) # creates giant list in memory

def make_list(num):
  result = []
  for i in range(num):
    result.append(i*2)
  return result

my_list = make_list(100)
print(my_list) 

# ----- Yield & Next -----

# generators are iterable
# only hold one item in memory
# yield - pauses function and comes back to it when we need to do something to it

def generator_function(num):
  for i in range(num):
    yield i*2

g = generator_function(100)
print(g) # <generator object generator_function at 0x10a74c900>
print(next(g)) # 0

next(g)
next(g)
print(next(g)) # 6
print(next(g)) # 8