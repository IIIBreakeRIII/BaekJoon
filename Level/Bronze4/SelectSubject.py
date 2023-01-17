# No. 11948 과목 선택

Science1 = int(input())
Science2 = int(input())
Science3 = int(input())
Science4 = int(input())
Social1 = int(input())
Social2 = int(input())

Science = [Science1, Science2, Science3, Science4]
Social = [Social1, Social2]

Science.sort(reverse=True)
Social.sort(reverse=True)

result = Science[0] + Science[1] + Science[2] + Social[0]

print(result)