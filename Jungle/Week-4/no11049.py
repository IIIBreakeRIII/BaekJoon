# No.11049 행렬 곱셈 순서

import sys
input = sys.stdin.readline

matrixes = int(input())

matrix_list = []

for i in range(matrixes):
    matrix_list.append(list(map(int, input().split())))

dp = [[0 for _ in range(matrixes)] for _ in range(matrixes)]

for i in range(1, matrixes):
    for j in range(0, matrixes - i):
        if i == 1:
            dp[j][j + i] = matrix_list[j][0] * matrix_list[j][1] * matrix_list[j + 1][1]
            continue

        dp[j][j + i] = 2 ** 32

        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + matrix_list[j][0] * matrix_list[k][1] * matrix_list[j + i][1])

print(dp[0][matrixes - 1])
