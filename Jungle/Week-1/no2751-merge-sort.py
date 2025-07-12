import sys

input = sys.stdin.readline

testcase = int(input())
num_list = []

for _ in range(testcase):
    num_list.append(int(input()))

def dividing(num_list):
    
    if len(num_list) <= 1:
        return num_list

    mid = len(num_list) // 2

    left_list = dividing(num_list[:mid])
    right_list = dividing(num_list[mid:])

    return merge(left_list, right_list)

def merge(left_list, right_list):
    result = []
    i = j = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1

    result.extend(left_list[i:])
    result.extend(right_list[j:])
    return result

result_list = dividing(num_list)

for i in result_list:
    print(i)
