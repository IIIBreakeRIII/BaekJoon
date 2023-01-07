N = int(input())
BeforeList = list(map(int, input().split()))

AfterList = []

MaxScore = max(BeforeList)

for i in range(N):
  AfterList.append(BeforeList[i] / MaxScore * 100)

print(sum(AfterList) / len(AfterList))