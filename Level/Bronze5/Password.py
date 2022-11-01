A = int(input())

for i in range(A):
  PW = input()
  PWList = list(map(str, str(PW)))
  if len(PWList) >= 6 and len(PWList) <= 9:
    print("yes")
  else:
    print("no")