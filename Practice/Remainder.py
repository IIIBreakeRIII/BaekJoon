# listNum = []
# listRemainder = []
# listRemainderTemp = []

# for i in range(10):
#   listNum.append(int(input()))

# for i in range(10):
#   listRemainder.append(listNum[i] % 42)
#   listRemainderTemp.append(listNum[i] % 42)

# for i in range(10):
#   j = i + 1
#   for j in range(j, 10):
#     if listRemainder[i] == listRemainder[j]:
#       print(i, "번 인덱스 탐색 중 : ", j, "번 인덱스 중복")
#       temp = listRemainder[j]
#       listRemainderTemp.remove(temp)
#     else:
#       continue

# print("Result")
# print(len(listRemainderTemp))

listNum = []

for i in range(1, 10):
  print("i = ", i)
  inputNum = int(input())
  Remainder = inputNum % 42
  listNum.append(Remainder)
  for j in range(len(listNum)):
    if len(listNum) == 1:
      print("첫번째 if, ", listNum)
      break
    elif listNum[j] == listNum[len(listNum) - 1]:
      print("두번째 if, 지우기 전 ", listNum)
      listNum.remove(listNum[len(listNum) - 1])
      print("두번째 if, 지우기 후 ", listNum)
    else:
      print("else break", listNum)
      break

print(listNum)

  # if i == 1:
  #   listNum.append(Remainder)
  #   print("추가됨"
  # else:
  #   for j in range(len(listNum)):
  #     print("-----j = ", j, "----")
  #     if Remainder == listNum[j - 1]:
  #       break
  #     else:
  #       listNum.append(Remainder)
  #       print(listNum)

print(len(listNum))

# listNum = []

# for i in range(10):
#   num = int(input())
#   remainder = num % 42
#   if remainder not in listNum:
#     listNum.append(remainder)

# print(len(listNum))