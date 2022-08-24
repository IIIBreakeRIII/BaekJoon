T = int(input())

Count = 1

for i in range(T):
  A, B = map(int, input().split())
  print("Case #{}:".format(Count), A + B)
  Count += 1