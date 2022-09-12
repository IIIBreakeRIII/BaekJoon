Score = []

for i in range(5):
  Score.append(int(input()))

for i in range(5):
  if Score[i] < 40:
    Score[i] = 40

print(sum(Score) // 5)