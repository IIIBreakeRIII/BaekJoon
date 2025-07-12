# 수 정렬하기 3
# Counting Sort

import sys

input = sys.stdin.readline

num = int(input())

num_list = [0] * 10001

for _ in range(num):
    n = int(input())
    num_list[n] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
