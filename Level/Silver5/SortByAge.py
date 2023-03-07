# No. 10814 나이순 정렬

Num = int(input())
List = []

for i in range(Num):
	Age, Name = input().split()
	Age = int(Age)
	List.append((Age, Name))

List.sort(key=lambda x:x[0])

for j in range(Num):
	print(List[j][0], List[j][1])
