# No.11725 트리의 부모 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1) 

def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)

dfs(1)

for x in range(2, n + 1):
    print(visited[x])
