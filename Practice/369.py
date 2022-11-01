A = int(input())
count = 0

for i in range(A + 1):
  NumberList = list(map(int, str(i)))
  for j in range(len(NumberList)):
    if NumberList[j] == 3:
      count += 1
    elif NumberList[j] == 6:
      count += 1
    elif NumberList[j] == 9:
      count += 1
    else:
      continue

print(count)