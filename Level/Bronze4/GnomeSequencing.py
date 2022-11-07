A = int(input())

print("Gnomes:")
for i in range(A):
  NumList = list(map(int, input().split()))
  if sorted(NumList, reverse=True) == NumList or sorted(NumList, reverse=False) == NumList:
    print("Ordered")
  else:
    print("Unordered")