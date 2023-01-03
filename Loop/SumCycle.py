Num = int(input())

left = Num // 10
right = Num % 10
cnt = 0
list = [left, right]

listA = [left, right]

while True:
  cnt = cnt + 1
  newRight = sum(listA) % 10
  listB = [listA[1], newRight]
  if list == listB:
    print(cnt)
    break
  else:
    listA = [listB[0], listB[1]]
    continue