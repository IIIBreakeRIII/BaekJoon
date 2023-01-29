# No. 2839 설탕배달

num = int(input())

if num % 5 == 3:
  print(num // 5 + 1)
else:
  A = num % 5
  A = A + 5
  if A % 3 == 0:
    print()