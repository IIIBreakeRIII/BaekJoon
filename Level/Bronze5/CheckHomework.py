numList = [i for i in range(1, 31)]

for _ in range(28):
  num = int(input())
  numList.remove(num)

print(min(numList))
print(max(numList))