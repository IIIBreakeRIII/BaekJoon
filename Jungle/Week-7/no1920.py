# No.1920 수 찾기

# import sys
# input = sys.stdin.readline
#
# count_of_n = int(input())
# n_list = set(map(int, input().split()))
#
# count_of_m = int(input())
# m_list = list(map(int, input().split()))
#
# for index in m_list:
#     if index in n_list:
#         print(1)
#     else:
#         print(0)

import sys
input = sys.stdin.readline

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return 0

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
arr2 = list(map(int, input().split()))


for x in arr2:
    if binary_search(x, arr):
        print(1)
    else:
        print(0)
