# No. 2675

N = int(input())

for i in range(N):
  repeatNum, inputList = input().split()
  divideString = list(inputList)
  
  for j in range(len(divideString)):
    print(divideString[j] * int(repeatNum), end="")
  
  print()