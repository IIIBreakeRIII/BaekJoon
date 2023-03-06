# No. 5635 생일

repeat = int(input())

StudentList = []

for i in range(repeat):
	Name, Day, Month, Year = input().split()
	Day, Month, Year = map(int, (Day, Month, Year))
	StudentList.append((Year, Month, Day, Name))

StudentList.sort()

print(StudentList[repeat - 1][3])
print(StudentList[0][3])
