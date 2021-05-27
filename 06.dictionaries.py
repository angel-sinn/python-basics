# not ordered like lists
# dictionary keys must be immutable

dictionary = {
  'a': 1,
  'b': 'hello',
  'c': [1,2,3]
}

print(dictionary) # {'a': 1, 'b': 'hello', 'c': [1, 2, 3]}
print(dictionary['b']) # hello

user = {
  'basket': [1,2,3],
  'greet': 'hello'
}

# get
print(user.get('age')) # None
print(user.get('age', 27)) # if age doesn't exist, use default 27

# dict - another way to create dictionary
user2 = dict(name = 'Angela')
print(user2) # {'name': 'Angela'}

# 'in'
print('basket' in user) # True

# keys
print('greet' in user.keys()) # True

# values
print('hello' in user.values()) # True

# items
print(user.items()) # dict_items([('basket', [1, 2, 3]), ('greet', 'hello')])

# clear
# print(user.clear()) # None

# copy
user3 = user.copy()
print(user) # {'basket': [1, 2, 3], 'greet': 'hello'}
print(user3) # {'basket': [1, 2, 3], 'greet': 'hello'}

# pop - removes key/value
print(user.pop('greet')) # hello
print(user) # {'basket': [1, 2, 3]}

# update
print(user.update({'basket': [0,1,2,3]})) # None
print(user) # {'basket': [0, 1, 2, 3]}