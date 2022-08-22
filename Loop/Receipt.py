sum = int(input())
num = int(input())
whole = 0

for i in range (num):
  object, price = map(int, input().split())
  whole += object * price
if whole == sum:
  print("Yes")
else:
  print("No")