N, M, K = map(int, input().split())

if N > M:
  N2 = N - K
  CompareN2 = N2 / 2
  if N2 <= 0:
    print(1//2)
  elif CompareN2 > M:
    print(M // 1)
  else:
    print(N2 // 2)
else:
  M2 = M - K
  if M2 <= 0:
    print(1//2)
  elif N > M2:
    i = N / 2
    if i > M2:
      print(M2 // 1)
    else:
      print(N // 2)
  else:
    print(N // 2)