listNum = []

for i in range(10):
  num = int(input())
  remainder = num % 42
  if remainder not in listNum:
    listNum.append(remainder)

print(len(listNum))