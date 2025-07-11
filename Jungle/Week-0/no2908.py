# No. 2908

NumA, NumB = map(int, input().split())

NewNumA = ((NumA % 10) * 100) + (NumA // 10 % 10) * 10 + (NumA // 100 % 10)
NewNumB = ((NumB % 10) * 100) + (NumB // 10 % 10) * 10 + (NumB // 100 % 10)

if NewNumA > NewNumB:
  print(NewNumA)
elif NewNumA == NewNumB:
  print(NewNumA)
else:
  print(NewNumB)
