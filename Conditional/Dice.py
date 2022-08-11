a, b, c = map(int, input().split())

if a == b == c:
  print(10000 + (a * 1000))
elif a == b:
  print(1000 + (a * 100))
elif b == c:
  print(1000 + (b * 100))
elif a == c:
  print(1000 + (a * 100))
else:
  max = a
  if max < b:
    max = b
  if max < c:
    max = c
  print(max * 100)

# max(a, b, c)으로 최댓값 추출 가능