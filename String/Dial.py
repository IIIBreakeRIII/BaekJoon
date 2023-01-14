# No. 5622

String = list(input())
cnt = 0

for i in range(len(String)):
  if String[i] == "A" or String[i] == "B" or String[i] == "C":
    cnt = cnt + 3
  elif String[i] == "D" or String[i] == "E" or String[i] == "F":
    cnt = cnt + 4
  elif String[i] == "G" or String[i] == "H" or String[i] == "I":
    cnt = cnt + 5
  elif String[i] == "J" or String[i] == "K" or String[i] == "L":
    cnt = cnt + 6
  elif String[i] == "M" or String[i] == "N" or String[i] == "O":
    cnt = cnt + 7
  elif String[i] == "P" or String[i] == "Q" or String[i] == "R" or String[i] == "S":
    cnt = cnt + 8
  elif String[i] == "T" or String[i] == "U" or String[i] == "V":
    cnt = cnt + 9
  elif String[i] == "W" or String[i] == "X" or String[i] == "Y" or String[i] == "Z":
    cnt = cnt + 10

print(cnt)