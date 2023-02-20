# No. 1316 그룹 단어 체커

# 내 풀이
############################################

# repeat = int(input())
# count = 0

# for i in range(repeat):
#     string = list(input())
#     newString = []

#     for j in range(len(string)):
#         if j == len(string) - 1:
#             if string[j] != string[j - 1]:
#                 newString.append(string[j])
#         elif string[j] != string[j + 1]:
#             newString.append(string[j])
#         else:
#             continue

#     for k in range(len(newString)):
#         for l in range(len(newString)):
#             if k >= l:
#                 continue
#             else:
#                 if newString[k] == newString[l]:
#                     count = count + 1
#                     break
#         break

# print(repeat - count)

############################################

# Google에서 내준 답

repeat = int(input())
GroupWord = 0

for _ in range(repeat):
    string = input()
    count = 0
    
    for i in range(len(string) - 1):             # 반복 생성
        if string[i] != string[i + 1]:          # i번째 문자와 i + 1번째 문자가 다를경우
            NewString = string[i + 1:]          # i + 1번째 문자부터 새로운 단어 생성
            
            if NewString.count(string[i]) > 0:  # 새로 생성한 단어에서 입력받은 단어의 i 번째 단어와 같은 단어가 있으면 count
                count = count + 1
    if count == 0:                              # count값이 없을 경우 즉 모든 단어가 그룹 단어가 아닐 경우
        GroupWord = GroupWord + 1

print(GroupWord)