# No. 1676 팩토리얼의 0의 개수

Num = int(input())
Sum = 1
count = 0

for i in range(1, Num + 1):
	Sum = Sum * i

SumList = list(map(int, str(Sum)))

SumList.reverse()

for j in range(len(SumList)):
	if SumList[j] == 0:
		count = count + 1
	elif SumList[j] != 0:
		break

print(count)
