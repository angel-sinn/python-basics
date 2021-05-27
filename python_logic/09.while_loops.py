i = 0
while i < 50:
  print(i)
  i += 1
else:
  print('Work is done!')

# using conditional with while loop
while True:
  response = input('Say something: ')
  if (response == 'Bye'):
    break

# continue
my_list = [1,2,3]
i = 0
while i < len(my_list):
  i += 1
  continue # goes back to the loop, won't hit next line
  print(my_list[i])