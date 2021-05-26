print(type("hi hello there!")) # <class 'str'>

username = 'angel'
password = 'secret'
long_string = '''
WOW
O O
---
'''

print(long_string)

# ----- Escape sequence -----
weather1 = "It's sunny"
weather2 = "It\'s \"kind of\" sunny"

print(weather1)
print(weather2)

# tab
weather3 = "\t It's sunny"

print(weather3)

# new line
weather4 = "It's sunny \nhope you have a good day!"

print(weather4)

# ----- Type conversion -----
print(type(str(100))) # <class 'str'>
print(type(int(str(100)))) # <class 'int'>

# ----- Formatted strings -----
name = 'Angel'
age = 27

print(f'Hi {name}. You are {age} years old.')
print('Hi {0}. You are {1} years old.'.format(name, age))

# ----- String indexes -----
random_string = '01234567'

print(random_string[0]) # 0
print(random_string[-1]) # 7

# [start:stop]
print(random_string[0:2]) # 01

# [start:stop:stepover]
print(random_string[0:8:2]) # 0246
print(random_string[1:]) # 1234567
print(random_string[:5]) #01234
print(random_string[::1]) #01234567

print(random_string[::-1]) # 76543210 -> reverse
print(random_string[::-2]) # 7531

# ----- String built-in functions & methods -----

# length (len)
greet = 'hellooo'
print(len('hellooo')) # 7

print(greet[0:len(greet)])

# uppercase (.upper())
quote = 'to be or not to be'

print(quote.upper()) # TO BE OR NOT TO BE

# lowercase (.lower())
quote = 'to be or not to be'

print(quote.lower()) # to be or not to be

# capitalize (.capitalize())

print(quote.capitalize()) # To be or not to be

# replace (.replace())
quote2 = quote.replace('be', 'me')

print(quote2)