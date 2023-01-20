# No. 2869 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())

NewHeight = V - A

if NewHeight % (A - B) != 0:
  print(NewHeight // (A - B) + 2)
else:
  print(NewHeight // (A - B) + 1)