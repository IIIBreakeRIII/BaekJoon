# No.2750 수 정렬하기

testcase = int(input())
num_list = []

for _ in range(testcase):
    num_list.append(int(input()))

num_list.sort()

for i in num_list:
    print(i)
