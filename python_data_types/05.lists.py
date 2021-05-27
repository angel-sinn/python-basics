# ----- List slicing ----- 
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'tablet']

print(amazon_cart[1]) # ['sunglasses']
print(amazon_cart[0::2]) # ['notebooks', 'toys']

amazon_cart[0] = 'laptops'
new_cart = amazon_cart[:] # use [:] or .copy so that original amazon_cart stays the same (copy vs overwriting)
# new_cart = amazon_cart.copy() # use [:] or .copy() so that original amazon_cart stays the same (copy vs overwriting)
new_cart[0] = 'gum'

print(new_cart) # ['gum', 'sunglasses', 'toys', 'tablet']
print(amazon_cart) # ['laptops', 'sunglasses', 'toys', 'tablet']

# ----- Matrix -----
matrix = [
  [1,2,1],
  [0,1,0],
  [1,0,1]
]

print(matrix[0][1]) # 2

# ----- List built-in functions & methods -----
basket = [1,2,3,4,5]

# append
new_list_append = basket.append(100)
print(basket) # [1, 2, 3, 4, 5, 100]
print(new_list_append) # None

# insert
new_list_insert = basket.insert(4, 100)
print(basket) # [1, 2, 3, 4, 100, 5, 100]
print(new_list_insert) # None

# extend
new_list_extend = basket.extend([101])
print(basket) # [1, 2, 3, 4, 100, 5, 100, 101]
print(new_list_extend) # None

# pop - give index, returns value removed
basket.pop()
print(basket) # [1, 2, 3, 4, 100, 5, 100]
basket.pop()
print(basket) # [1, 2, 3, 4, 100, 5]
new_list_pop = basket.pop(4)
print(basket) # [1, 2, 3, 4, 5]
print(new_list_pop) # 100

# remove - give value
basket.remove(5)
print(basket) # [1, 2, 3, 4]

#clear
basket.clear()
print(basket) # []

# index
basket_letters = ['a', 'b', 'c', 'd', 'e', 'a']
print(basket_letters.index('b', 0, 5)) # 1

# 'in'
print('b' in basket_letters) # true
print('x' in basket_letters) # false

print('i' in 'Hi my name is Angel') # true

# count
print(basket_letters.count('b')) # 1

# sort
basket_letters.sort()
print(basket_letters) # ['a', 'a', 'b', 'c', 'd', 'e']

# sorted - returns new array
print(sorted(basket_letters)) # ['a', 'a', 'b', 'c', 'd', 'e']

# reverse
basket_letters.reverse()
print(basket_letters) # ['e', 'd', 'c', 'b', 'a', 'a']

# list slicing makes copy of list
print(basket_letters[::-1]) # ['a', 'a', 'b', 'c', 'd', 'e']

print(basket_letters) # ['e', 'd', 'c', 'b', 'a', 'a']

# range
print(list(range(1,100))) # list from 1-99
print(list(range(101))) # list from 0-100

# join - list to string
new_sentence = ' '.join(['Hi', 'my', 'name', 'is', 'Angel'])

print(new_sentence) # Hi my name is Angel

# ----- List Unpacking -----
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a) # 1
print(b) # 2
print(c) # 3
print(other) # [4, 5, 6, 7, 8, 9]
print(d) # 9

