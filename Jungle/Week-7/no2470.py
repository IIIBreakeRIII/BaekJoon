# No.2470 두 용액
# Use two pointer for pointing first index and last index
# +1 to first index(pointer) and -1 to last index(pointer)

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_sum = float("inf")
result = [0, 0]

start = 0
end = n - 1

while start < end:
    current_sum = arr[start] + arr[end]

    if abs(current_sum) < min_sum:
        min_sum = abs(current_sum)
        result = [arr[start], arr[end]]

    if current_sum > 0:
        end -= 1
    elif current_sum < 0:
        start += 1
    else:
        break

print(*result)
