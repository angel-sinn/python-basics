# ----- Exercise 1 -----
birth_year = input('What year were you born?')
age = 2021 - int(birth_year) # must convert input to int first

print(f'Your age is: {age}')

# ----- Exercise 2 -----

username = input('What is your username?')
password = input('What is your password?')
password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password {hidden_password} is {password_length} characters long')