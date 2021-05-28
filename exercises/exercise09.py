# ----- Exercise 9 -----
class Cat:
  species = 'mammal'
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Instantiate the Cat object with 3 cats
cat1 = Cat("cat1", 3)
cat2= Cat("cat2", 2)
cat3 = Cat("cat3", 5)

# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)

# Output
print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")