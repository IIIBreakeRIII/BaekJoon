while True:
  Num = int(input())
  Star = "*"
  if Num == 0:
    break
  else:
    for i in range(Num + 1):
      if i == 0:
        continue
      else:
        print(Star * i)