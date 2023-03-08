# No. 2535 아시아 올림피아드

Num = int(input())

StudentList = []
PrizeList = []

for i in range(Num):
	Country, StudentNum, Score = input().split()
	StudentList.append((Country, StudentNum, Score))

StudentList.sort(key=lambda x:x[2], reverse=True)

PrizeList.append(StudentList[0])
PrizeList.append(StudentList[1])
PrizeList.append(StudentList[2])

for j in range(3):
	del StudentList[0]

while True:
	if PrizeList[0][0] == PrizeList[1][0] == PrizeList[2][0]:
		del PrizeList[2]
		PrizeList.append(StudentList[0])
		del StudentList[0]
	else:
		break

for k in range(3):
	print(PrizeList[k][0], PrizeList[k][1])
