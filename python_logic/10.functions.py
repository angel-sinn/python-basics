def say_hello():
  print('hello')

say_hello()

# parameters 
def say_goodbye(name, emoji):
  print(f'Goodbyeeee {name} {emoji}')

# default parameters
def say_goodbye2(name='Bob', emoji='😎'):
  print(f'Goodbyeeee {name} {emoji}')

say_goodbye2()

# positional arguments
say_goodbye('Angel', '😁')
say_goodbye('Angela', '😁')

# keyword arguments - not best practice
say_goodbye(emoji='😁', name="Angelaa")