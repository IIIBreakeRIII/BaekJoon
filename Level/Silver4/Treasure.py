# No. 1026 보물

Num = int(input())
ListA = list(map(int, input().split()))
ListB = list(map(int, input().split()))

Sum = 0
SortListA = []
SortListB = []

for i in range(Num):
	SortListA.append(ListA[i])
	SortListB.append(ListB[i])

SortListA.sort()
SortListB.sort(reverse=True)

for j in range(Num):
	Sum = Sum + (SortListA[j] * SortListB[j])

print(Sum)
