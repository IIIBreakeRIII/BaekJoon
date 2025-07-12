Num = int(input())

WordList = []
Result = []

for i in range(Num):
	WordList.append(input())

WordList.sort()
WordList.sort(key = len)

for tmp in WordList:
	if tmp not in Result:
		Result.append(tmp)

for j in range(len(Result)):
	print(Result[j])

