# No. 1120 문자열

A, B = map(str, input().split())

A_List = list(A)
B_List = list(B)

count = 0
ans = []

if len(A_List) == len(B_List):
	for i in range(len(A_List)):
		if A_List[i] != B_List[i]:
			count = count + 1
		else:
			continue
	ans.append(count)

else:
	for i in range(len(B_List) - len(A_List) + 1):
		tmp = 0
		count = 0
		tmp = tmp + i
		for j in range(len(A_List)):
			if A_List[j] != B_List[tmp]:
				count = count + 1
			else:
				pass
			tmp = tmp + 1
		ans.append(count)

print(min(ans))
