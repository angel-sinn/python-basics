# everything in python is an object

# class: blueprint, object: instances
# constructor/init method __init__

class PlayerCharacter:
  # class object attribute (static)
  membership = True

  def __init__(self, name, age):
      # class attribute (dynamic) - need to use self
      self.name = name
      self.age = age
  
  def shout(self):
    print(f'My name is {self.name}')

  # method - decorator
  @classmethod
  def adding_things(cls, num1, num2):
    return cls('Teddy', num1 + num2)
  
  # static - no access to cls
  @staticmethod
  def adding_things2(num1, num2):
    return num1 + num2

player1 = PlayerCharacter('Angel', 27)
player2 = PlayerCharacter('Angela', 28)

print(player1.name, player1.age) # Angel 27
print(player2.name, player2.age) # Angela 28

print(player1.membership) # True
print(player2.membership) # True

print(player1.shout()) # My name is Angel
print(player2.shout())  # My name is Angela

player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)