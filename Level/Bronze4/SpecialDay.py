Month = int(input())
Day = int(input())

if Month > 2:
  print("After")
elif Month == 2:
  if Day > 18:
    print("After")
  elif Day == 18:
    print("Special")
  else:
    print("Before")
else:
  print("Before")