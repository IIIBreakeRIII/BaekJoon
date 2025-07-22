# No.2493 탑

import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
stack = []
answer = [0] * n

for i in range(n):
    current_height = tops[i]
    
    while stack and stack[-1][1] < current_height:
        stack.pop()
    
    if stack:
        answer[i] = stack[-1][0] + 1
    
    stack.append((i, current_height))

print(*answer)
