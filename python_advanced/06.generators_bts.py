# ----- For loops bts -----
def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try: 
      print(iterator)
      print(next(iterator))
    except StopIteration: 
      break


special_for([1,2,3])

# <list_iterator object at 0x1033aae50> 1
# <list_iterator object at 0x1033aae50> 2
# <list_iterator object at 0x1033aae50> 3

# ----- Generators(range) bts -----
class MyGen():
  current = 0

  def __init__(self, first, last):
    self.first = first
    self.last = last
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration
    
gen = MyGen(0,100)
for i in gen:
  print(i)