# gives index (i) counter by unpacking

for i, char in enumerate('Hellooo'):
  print(i, char)

for i, number in enumerate((1,2,3)):
  print(i, number)

for i,char in enumerate(list(range(100))):
  if char == 50:
    print(f'Index of 50 is: {i}')