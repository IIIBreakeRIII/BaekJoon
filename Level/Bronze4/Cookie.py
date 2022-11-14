K, N, M = map(int, input().split())

Money = K * N - M

if Money >= 0:
  print(Money)
else:
  print(0)