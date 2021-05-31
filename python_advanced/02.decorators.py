def my_decorator(func):
  def wrap_func():
    print('*********')
    func()
    print('*********')
  return wrap_func

@my_decorator
def hello():
  print('hellooooo') # ********* hellooooo *********

@my_decorator
def bye():
  print('see you!') 

hello() # ********* hellooooo *********
bye() # ********* see you! *********

# ----- Keyword arguments -----
def my_decorator2(func):
  def wrap_func(*args, **kwargs):
    print('*********')
    func(*args, **kwargs)
    print('*********')
  return wrap_func

@my_decorator2
def hello2(greeting, emoji=':('):
  print(greeting, emoji)

hello2('hiii') # ********* hiii :( *********

# ----- Performance decorator example -----
from time import time

def performance(func):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()
    print(f'It took {t2-t1} ms')
    return result
  return wrapper

@performance
def long_time():
  for i in range(1000000):
    i * 5

long_time() # It took 0.1319260597229004 ms