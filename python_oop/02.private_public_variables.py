# python doesn't support public/private
# use _ to indicate private variable
# use __ (dundar method) to indicate not to modify

class PlayerCharacter:
  def __init__(self, name, age):
      self._name = name
      self._age = age
  
  def run(self):
    print('run')

  def speak(self):
    print(f'My name is {self._name}, and I am {self._age} yeras old')

player1 = PlayerCharacter('Angel', 27)
player1.name = '!!!'
player1.speak = 'WOWWWW'

print(player1.speak)