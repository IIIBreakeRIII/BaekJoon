# No.11279 최대 힙

import sys
import heapq
input = sys.stdin.readline

n_count = int(input())
num_list = []

for _ in range(n_count):
    temp = int(input())
    
    if temp > 0:
        heapq.heappush(num_list, -temp)
    else:
        if not num_list:
            print(0)
        else:
            print(-heapq.heappop(num_list))
