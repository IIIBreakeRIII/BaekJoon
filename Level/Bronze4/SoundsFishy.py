A = int(input())
B = int(input())
C = int(input())
D = int(input())

DepthList = [A, B, C, D]

if DepthList[0] < DepthList[1] and DepthList[1] < DepthList[2] and DepthList[2] < DepthList[3]:
  print("Fish Rising")
elif DepthList[0] > DepthList[1] and DepthList[1] > DepthList[2] and DepthList[2] > DepthList[3]:
  print("Fish Diving")
elif max(DepthList) == min(DepthList):
  print("Fish At Constant Depth")
else:
  print("No Fish")