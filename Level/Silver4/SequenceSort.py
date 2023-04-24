# No. 1015 수열 정렬

N = int(input())
A_List = list(map(int, input().split()))

B_List = sorted(A_List)
P_List = []

for i in range(N):
	temp = index = 0
	temp = A_List[i]
	index = B_List.index(temp)
	B_List[index] = 0
	P_List.append(index)

for j in range(len(P_List)):
	print(P_List[j], end=" ")
