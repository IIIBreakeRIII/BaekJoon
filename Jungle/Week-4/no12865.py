# No.12865 평범한 배낭

import sys
input = sys.stdin.readline

# 물품 수 n, 버틸 수 있는 무게 k
n, k = map(int, input().split())

# 물건 리스트
things = []

# 물건 무게 w, 가치 v
for _ in range(n):
    w, v = map(int, input().split())
    things.append([w, v])

# memoization
memo = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = things[i - 1][0]
        value = things[i - 1][1]

        if j < weight:
            memo[i][j] = memo[i - 1][j]
        else:
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - weight] + value)

print(memo[n][k])
