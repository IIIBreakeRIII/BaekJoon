# No. 1712 손익 분기점

# 첫번째 풀이, 런타임에러(ZeroDivisionError)

# A, B, C = map(int, input().split())

# if A // (C - B) <= 0:
#   print("-1")
# else:
#   print ((A // (C - B)) + 1)

A, B, C = map(int, input().split())

try:
  Result = A // (C - B)
except ZeroDivisionError:
  Result = -1

if Result < 0:
  Result = -1
else:
  Result = Result + 1

print(Result)