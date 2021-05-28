# Dunder Methods - contract between the person who implemented a certain class and the Python interpreter, which knows when to call that particular dunder method.

# also called Magic Methods - Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action. 

# In order to make the overloaded behaviour available in your own custom class, the corresponding magic method should be overridden. 

class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
      'name': 'Angel',
      'has_pets': False
    }

  def __str__(self):
    return f'{self.color}'

  def __len__(self):
    return 5
  
  def __call__(self):
    return('called!')

  def __getitem__(self, i):
    return self.my_dict[i]

  def __del__(self):
    print('deleted!')

action_figure = Toy('red', 0)

print(action_figure.__str__()) # red
print(str(action_figure)) # red
print(str('action_figure')) # action_figure

print(len(action_figure)) # 5

print(action_figure()) # called!

print(action_figure['name']) # Angel

del action_figure # deleted!
