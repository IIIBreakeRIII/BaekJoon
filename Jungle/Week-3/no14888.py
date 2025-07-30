import sys

input = sys.stdin.readline

count = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -int(1e9)
min_result = int(1e9)

def DFS(add, sub, mul, div, sum, index):
    global max_result, min_result

    if index == count:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return

    if add:
        DFS(add - 1, sub, mul, div, sum + number[index], index + 1)
    if sub:
        DFS(add, sub - 1, mul, div, sum - number[index], index + 1)
    if mul:
        DFS(add, sub, mul - 1, div, sum * number[index], index + 1)
    if div:
        DFS(add, sub, mul, div - 1, int(sum / number[index]), index + 1)

DFS(add, sub, mul, div, number[0], 1)

print(max_result)
print(min_result)
