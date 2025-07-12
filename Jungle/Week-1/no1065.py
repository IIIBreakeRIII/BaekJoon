# No. 1065 한수

num = int(input())

count = 0

if num < 100:
	print(num)

elif num >= 100:
	count = 99
	temp = 100
	while(True):
		if temp - 1 == num:
			break
		else:
			Num_List = list(map(int, str(temp)))
			if Num_List[1] - Num_List[0] == Num_List[2] - Num_List[1]:
				count = count + 1
			temp = temp + 1

	print(count)
