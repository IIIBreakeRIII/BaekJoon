# No.17608 막대기

import sys

input = sys.stdin.readline

count = int(input())
stick_list = []

for _ in range(count):
    stick_list.append(int(input()))

max = 0
ans = 0

for stick in reversed(stick_list):
    if stick > max:
        max = stick
        ans += 1

print(ans)
