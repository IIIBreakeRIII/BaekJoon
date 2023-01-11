# No. 1157

A = input().upper()
Word = list(A)
WordList = []

# for i in range(len(Word)):
#   if i == 0:
#     WordList.append(Word[i])
#   elif i != 0:
#     for j in range(len(Word)):
#       if Word[i] == Word[j]:
#         if i >= j:
#           break
#         else:
#           print(i, "번 인덱스 = ", Word[i], "중복")
#       else:
#         if i >= j:
#           break
#         else:
#           WordList.append(Word[i])

for i in range(len(Word)):
  if i == 0:
    WordList.append(Word[i])
  elif i != 0:
    for j in range(len(Word)):
      if i == j:
        print("i == j 조건, i = ", i, "j = ", j)
        break
      elif i > j:
        if Word[i] == Word[j]:
          print("인덱스 : ", j, "번 -> 같은 단어 : ", Word[j])
        else:
          for k in range(len(WordList)):
            if WordList[k] == Word[i]:
              break
            else:
              WordList.append(Word[i])
      else:
        print("i가 j보다 작은 경우, i = ", i, "j = ", j)
        break


print("원래 단어 = ", Word)
print("중복 단어 = ", WordList)