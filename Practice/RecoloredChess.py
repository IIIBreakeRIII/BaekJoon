Row, Column = map(int, input().split())

chess = []

for i in range(Row):
  Text = input()
  chess.append(list(Text))

count = 0

if chess[0][0] == "W":
  for i in range(Row):
    if i % 2 == 0:  #짝수
      for j in range(Column):
        if j % 2 == 0:
          if chess[i][j] == "B":
            count = count + 1
        else:
          if chess[i][j] == "W":
            count = count + 1
    else: #홀수
      for j in range(Column):
        if j % 2 == 0:
          if chess[i][j] == "W":
            count = count + 1
        else:
          if chess[i][j] == "B":
            count = count + 1
elif chess[0][0] == "B":
  for i in range(Row):
    if i % 2 == 0:  #짝수
      for j in range(Column):
        if j % 2 == 0:
          if chess[i][j] == "W":
            count = count + 1
        else:
          if chess[i][j] == "B":
            count = count + 1
    else: #홀수
      for j in range(Column):
        if j % 2 == 0:
          if chess[i][j] == "B":
            count = count + 1
        else:
          if chess[i][j] == "W":
            count = count + 1

print(count)