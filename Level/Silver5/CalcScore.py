# No. 2822 점수 계산

ScoreList = []
NewScoreList = []
List = []
AllScore = 0

for i in range(8):
    temp = int(input())
    ScoreList.append(temp)
    NewScoreList.append(temp)

ScoreList.sort(reverse=True)

for j in range(5):
    AllScore = AllScore + ScoreList[j]
    List.append(NewScoreList.index(ScoreList[j]))

print(AllScore)

List.sort()

for k in range(len(List)):
    print(List[k] + 1, end=" ")
