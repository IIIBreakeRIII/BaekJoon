# No. 1427 소트인사이드

NumList = list(map(int, str(input())))

NumList.sort(reverse=True)

for i in range(len(NumList)):
    print(NumList[i], end="")
