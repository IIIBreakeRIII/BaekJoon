listNum = []

for i in range(9):
  listNum.append(int(input()))

print(max(listNum))
print(listNum.index(max(listNum)) + 1)