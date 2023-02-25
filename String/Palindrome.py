Word = input()

WordList = list(Word)
NewWordList = []

for i in reversed(range(len(WordList))):
    NewWordList.append(WordList[i])

if WordList == NewWordList:
    print("1")

else:
    print("0")