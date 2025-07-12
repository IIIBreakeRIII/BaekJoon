# No.2751 수 정렬하기 2
# Merge Sort로 다시 풀 것

testcase = int(input())
num_list = []

for _ in range(testcase):
    num_list.append(int(input()))

num_list.sort()
    
for i in range(testcase):
    print(num_list[i])
