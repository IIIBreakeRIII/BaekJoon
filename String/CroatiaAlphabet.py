# No. 2941

String = input()
StringList = list(String)

for i in range(len(StringList)):
  if StringList[i] == "=" or StringList[i] == "-":
    if i == 1:
      StringList[i] = "0"
    elif i >= 2:
      if StringList[i - 1] == "z" and StringList[i - 2] == "d":
        StringList[i] = "0"
        StringList[i - 1] = "0"
      else:
        StringList[i] = "0"
  elif StringList[i] == "j":
    if i == 0:    # i가 첫번째 인덱스이면 그냥 넘김
      continue
    else:
      if StringList[i - 1] == "l" or StringList[i - 1] == "n":
        StringList[i] = "0"
        
cnt = len(StringList) - StringList.count("0")
print(cnt)

# 아래 코드는 첫 시도, 백준에서 인덱스 에러
# 내가 보기엔 만약에 list[i]가 리스트 마지막 원소에 도달했을 경우,
# i + 1, i + 2의 값이 없어서 벌어지는 에러인 느낌
# 따라서 위의 코드로 수정

# for i in range(0, len(StringList)):
#   if StringList[i] == "=" or StringList[i] == "-":
#     StringList[i] = "0"
#   elif StringList[i] == "d":
#     if StringList[i + 1] == "z":
#       if StringList[i + 2] == "=":
#         StringList[i + 1] = "0"
#         StringList[i + 2] = "0"
#   elif StringList[i] == "l":
#     if StringList[i + 1] == "j":
#       StringList[i + 1] = "0"
#   elif StringList[i] == "n":
#     if StringList[i + 1] == "j":
#       StringList[i + 1] = "0"

# cnt = len(StringList) - StringList.count("0")
# print(StringList)
# print(cnt)