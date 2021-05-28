# global keyword
total = 0

def count():
  global total # declare we are using global total variable
  total += 1
  return total

count()
count()
print(count())

# nonlocal keyword
def outer():
  x = "local"
  def inner():
    nonlocal x
    x = "nonlocal"
    print("inner: ", x) # inner: nonlocal
  
  inner()
  print("outer: ", x) # outer: nonlocal

outer()