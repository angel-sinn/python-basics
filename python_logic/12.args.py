# *args

def super_func(*args):
  print(args)
  return sum(args)

super_func(1,2,3,4,5) # (1,2,3,4,5)
print(super_func(1,2,3,4,5)) # (1,2,3,4,5) 15

# **kwargs
def super_func2(*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func2(1,2,3,4,5, num1=5, num2=10)) # 30

# Rule: params, *args, default parameters, **kwargs