# No. 2261 가장 가까운 두 점
from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
n_list = []

for _ in range(n):
    x, y = map(int, input().strip().split())
    n_list.append((x, y))

min_dist = float('inf')

for a, b in combinations(n_list, 2):
    dist = (a[0] - b[0])**2 + (a[1] - b[1])**2
    if dist < min_dist:
        min_dist = dist

print(min_dist)
