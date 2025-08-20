# No.10971 외판원 순회 2

import sys
import itertools

input = sys.stdin.readline

n = int(input())
visiting_cost = []

for _ in range(n):
    visiting_cost.append(list(map(int, input().split())))

def find_min_cost(arr):
    cities = [city for city in range(n)]
    min_cost = float('inf')
    
    # get all case of route using permutation
    for i in itertools.permutations(cities):
        visit_case = list(i)
        visit_case.append(i[0])
        cost = 0
        
        # get departure and arrival using index & index + 1
        for j in range(n):
            departure = visit_case[j]
            arrival = visit_case[j + 1]
            
            # if departure == arrival return 0
            if arr[departure][arrival] == 0:
                cost = float('inf')
                break
            
            cost += arr[departure][arrival]

        min_cost = min(min_cost, cost)

    print(min_cost)

find_min_cost(visiting_cost)
