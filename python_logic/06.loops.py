# string
for item in '12345':
  print(item)

# set
for item in {1,2,3,4,5}:
  print(item)

# tuple
for item in (1,2,3,4,5):
  print(item)

# list
for item in [1,2,3,4,5]:
  print(item)

# nesting loops
for item in (1,2,3,4,5):
  for x in ['a', 'b', 'c']:
    print(item, x)

# dictionary
user = {
  'name': 'Angel',
  'age': 27,
  'can_swim': False
}

for item in user.keys():
  print(item) # name age can_swim

for item in user.values():
  print(item)  # Angel 27 False

for item in user.items():
  print(item) # ('name', 'Angel') ('age', 27) ('can_swim', False)

  key, value = item
  print(key, value) # name Angel age 27 can_swim False

# short hand version / more common
for key, value in user.items():
  print(key, value) # name Angel age 27 can_swim False