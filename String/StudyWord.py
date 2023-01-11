# No. 1157

Word = input().upper()
WordList = list(set(Word))    # 입력받은 문자에서 중복값을 제거

cntList = []

for i in WordList:
  cnt = Word.count(i)
  cntList.append(cnt)

if cntList.count(max(cntList)) >= 2:
  print("?")
else:
  maxIndex = cntList.index(max(cntList))
  print(WordList[maxIndex])