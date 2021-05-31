# try, except, else, finally (runs every time)
# use while loops

while True:
  try:
    age = int(input('What is your age? '))
    print(age)
    10/age # test if age is 0 -> zero division error
  except ValueError: 
    print('Please enter a number!')
    continue
  except ZeroDivisionError: 
    print('Please enter age higher than 0')
    continue
  else: 
    print('Thank you!')
    break
  finally: 
    print('Prints every time')

# ---- As err (using variable) -----

def sum(num1, num2):
  try: 
    return num1 + num2
  except TypeError as err: 
    print(f'Please enter numbers: {err}')
  
print(sum('1', 2)) # Please enter numbers: can only concatenate str (not "int") to str
print(sum(1, 2)) # 3

# ----- Wrap multiple errors -----

def divide(num1, num2):
  try: 
    return num1/num2
  except (TypeError, ZeroDivisionError) as err: 
    print(err)
  
print(divide('2', 1)) # unsupported operand type(s) for /: 'str' and 'int'
print(divide(2, 1)) # 2.0
print(divide(2, 0)) # division by zero