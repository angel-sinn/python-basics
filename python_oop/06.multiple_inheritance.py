class User():
  def sign_in(self):
    print('Logged in')

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'Attacking with power of {self.power}') 

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def check_arrows(self):
    print(f'{self.num_arrows} remaining')
  
  def run(self):
    print('Runs really fast')

# multiple inheritance
class HybridBorg(Wizard, Archer):
  def __init__(self, name, power, num_arrows):
    Wizard.__init__(self, name, power)
    Archer.__init__(self, name, num_arrows)

hybridBorg1 = HybridBorg('Borgborg', 50, 100)

print(hybridBorg1.run()) # Runs really fast
print(hybridBorg1.check_arrows()) # 100 remaining
print(hybridBorg1.attack()) # Attacking with power of 50
print(hybridBorg1.sign_in()) # Logged in



