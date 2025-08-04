# No.9084 동전

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    coins.insert(0, 0)
    print(coins)
    M = int(input())

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N+1):
        dp[i][0] = 1

    for j in range(1, N + 1):
        for i in range(1, M + 1):
            dp[j][i] = dp[j - 1][i]

            if i - coins[j] >= 0:
                dp[j][i] += dp[j][i - coins[j]]

    print(dp[N][M])
