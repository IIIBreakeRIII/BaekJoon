# No. 2292 벌집

Num = int(input())

InitRoom = 1
count = 1

if Num == 1:
  print(1)
else:
  while True:
    if Num > InitRoom and Num <= InitRoom + (6 * count):
      print(count + 1)
      break
    else:
      InitRoom = InitRoom + (6 * count)
      count = count + 1