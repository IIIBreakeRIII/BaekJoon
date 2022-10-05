N = int(input())
Nums = list(map(int, input().split()))
V = int(input())

count = 0

for i in range(len(Nums)):
  if Nums[i] == V:
    count += 1

print(count)