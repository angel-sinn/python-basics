# ----- Exercise 11 -----
# make list a parent class - inheritance

class SuperList(list):
  def __len__(self):
   return 1000

superlist1 = SuperList()

print(len(superlist1)) # 1000
superlist1.append(5)
print(superlist1[0]) # 5
print(issubclass(SuperList, list)) # True
print(issubclass(list, object)) # True