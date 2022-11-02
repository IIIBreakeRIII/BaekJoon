while True:
  A = input()
  if A == "#":
    break
  count = 0
  WordList = list(map(str, str(A)))
  for i in range(len(WordList)):
    if WordList[i] == "a" or WordList[i] == "A":
      count += 1
    elif WordList[i] == "e" or WordList[i] == "E":
      count += 1
    elif WordList[i] == "i" or WordList[i] == "I":
      count += 1
    elif WordList[i] == "o" or WordList[i] == "O":
      count += 1
    elif WordList[i] == "u" or WordList[i] == "U":
      count += 1
    else:
      continue
  print(count)