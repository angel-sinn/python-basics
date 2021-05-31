# functions - first class citizens (can act like variables)
# decorators supercharge our functions and add extra functionality

#@decorator
def hello(func):
 func()

def greet():
  print('hellooo')

a = hello(greet)

print(a)

# ----- Higher Order Function HOC -----
# 1. function that accepts another function (map, filter, reduce, etc)
def greet1(func):
  func()

# 2. function that returns another function
def greet2():
  def func():
    return 5
  return func
