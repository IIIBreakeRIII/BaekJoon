# No.2805 나무 자르기

import sys
input = sys.stdin.readline

tree_count, necessary_tree = map(int, input().split())
tree_list = list(map(int, input().split()))

start, end = 1, max(tree_list)

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for tree in tree_list:
        if tree > mid:
            sum += tree - mid

    if sum < necessary_tree:
        end = mid - 1
    else:
        start = mid + 1

print(end)

