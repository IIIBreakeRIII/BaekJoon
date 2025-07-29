# No.1260 DFS와 BFS

import sys
import collections

input = sys.stdin.readline

vertices, edges, num = map(int, input().split())
graph = [[] for _ in range(vertices + 1)]

for i in range(edges):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for index in graph:
    index.sort()

def dfs(graph, start):
    visited = [False] * (vertices + 1)
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            print(node, end=' ')
            visited[node] = True
            stack.extend(sorted([x for x in graph[node] if not visited[x]], reverse=True))

def bfs(graph, start):
    visited = [False] * (vertices + 1)
    queue = collections.deque([start])

    visited[start] = True

    while queue:

        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


dfs(graph, num)
print()
bfs(graph, num)
