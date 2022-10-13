N, M, K = map(int, input().split())

ResultN = K // M
ResultM = K % M

print(ResultN, ResultM)