# Lambda expressions - an anonymous function or a function having no name. Only use them once.

# lambda param: action(param)

from functools import reduce

my_list = [1,2,3]

print(list(map(lambda item: item * 2, my_list))) # [2,4,6]

print(list(filter(lambda item: item % 2 != 0, my_list))) # [1,3]

print(reduce(lambda acc, item: acc + item, my_list)) # 6