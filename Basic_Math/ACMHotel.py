# No. 10250 ACM 호텔

Testcase = int(input())

for i in range(Testcase):
  H, W, N = map(int, input().split())

  floor = N % H
  roomNum = N // H + 1

  if floor == 0:
    floor = H
    roomNum = N // H
    
  if roomNum < 10:
    print("{}0{}".format(floor,roomNum))
  else:
    print("{}{}".format(floor, roomNum))