# No.10971
# 외판원 순회 2

from itertools import permutations

N = int(input())
data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

def func(arr):
    cities = [city for city in range(N)]
    min_cost = float('inf')

    for p in permutations(cities):
        permu = list(p)
        permu.append(p[0])
        cost = 0

        for n in range(N):
            i = permu[n]
            j = permu[n + 1]

            if arr[i][j] == 0:
                cost = float('inf')
                break

            cost += arr[i][j]

        min_cost = min(min_cost,cost)
        
    print(min_cost)

func(data)
