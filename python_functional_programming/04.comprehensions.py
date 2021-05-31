# ----- List Comprehensions -----
my_list = []

for char in 'hello':
  my_list.append(char)

print(my_list) # ['h', 'e', 'l', 'l', 'o']

my_list1 = [char for char in 'hello']
print(my_list1) # ['h', 'e', 'l', 'l', 'o']

my_list2 = [num for num in range(0,100)]
print(my_list2)

# add expression
my_list3 = [num*2 for num in range(0,100)]
print(my_list3)

# add conditional
my_list4 = [num*2 for num in range(0,100) if num % 2 == 0]
print(my_list4)

# ----- Set Comprehensions -----
my_set = {char for char in 'hello'}
print(my_set) # {'h', 'o', 'l', 'e'} - unordered data structure so not guaranteed to be hello, sets remove duplicates also

my_set1 = {num for num in range(0,100)}
print(my_set1)

# ----- Dict Comprehensions -----
simple_dict = {
  'a': 1,
  'b': 2
}

my_dict = {key:value * 2 for key, value in simple_dict.items()}
print(my_dict) # {'a': 2, 'b': 4}

my_dict1 = {key:value * 2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict1) # {'b': 4}

my_dict2 = {num: num* 2 for num in [1,2,3]}
print(my_dict2) # {1: 2, 2: 4, 3: 6}