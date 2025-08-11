# No.2751 수 정렬하기 2

import sys
input = sys.stdin.readline

tc = int(input())

num_list = []

for _ in range(tc):
    num_list.append(int(input()))

def divide(num_list):
    
    # return condition
    if len(num_list) <= 1:
        return num_list

    mid = len(num_list) // 2
    
    # call recursion for divide
    left_list = divide(num_list[:mid])
    right_list = divide(num_list[mid:])
    
    # if divide finish, call merge
    return merge(left_list, right_list)

def merge(left_list, right_list):
    result = []

    # declare pointer
    i = j = 0
    
    # repeat until one of the list is empty
    while i < len(left_list) and j < len(right_list):

        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1

        else:
            result.append(right_list[j])
            j += 1

    # add all of the last things in each list
    result.extend(left_list[i:])
    result.extend(right_list[j:])

    return result

result_list = divide(num_list)

for i in result_list:
    print(i)
