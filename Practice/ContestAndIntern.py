N, M, K = map(int, input().split())

if N > M:
  A = N - K   #많은 애에서 인턴 빼기
  i = N / 2   #
  if i > A:
    Team = M // 1
    print(Team)
  else:
    Team = A // 2
    print(Team)
else:
  A = M - K
  if N > A:
    i = N / 2
    if i > A:
      Team = A // 1
      print(Team)
    else:
      Team = N // 2
      print(Team)
  else:
    Team = N // 2
    print(Team)