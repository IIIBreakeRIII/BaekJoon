BottleList = list(map(int, input().split()))
Sum = 0

for i in range(len(BottleList)):
  Sum += BottleList[i] * 5

print(Sum)