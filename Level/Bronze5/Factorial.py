A = int(input())
result = 1
i = 0

for i in range (1, A + 1):
  result = result * i
  i += 1

print(result)