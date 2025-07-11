testcase = int(input())

for i in range(testcase):
  ScoreList = list(map(int, input().split()))
  cnt = 0
  SumScore = sum(ScoreList) - ScoreList[0]
  Average = SumScore / ScoreList[0]

  for j in range(len(ScoreList)):
    if ScoreList[j] == ScoreList[0]:
      continue
    else:
      if ScoreList[j] > Average:
        cnt = cnt + 1
      else:
        continue

  print("{:.3f}%".format(cnt / ScoreList[0] * 100))
