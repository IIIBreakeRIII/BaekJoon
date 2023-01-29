# No. 2775 부녀회장이 될테야
# 도전중

testcase = int(input())

for i in range(testcase):
  floor = int(input())
  num = int(input())

  if floor == 0:
    print(num)
  else:
    if num == 1:
      print("1")
    elif num == 2:
      print(floor + num)
