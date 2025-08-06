# No.11047 동전 0

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

answer = 0

for i in coins:
  answer += K // i
  K = K % i
 
print(answer)
