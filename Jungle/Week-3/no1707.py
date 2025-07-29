# No.1707 이분 그래프

import collections
import sys

input = sys.stdin.readline

def BFS(graph, vertices):
    visited = [0 for _ in range(vertices + 1)]

    for i in range(1, vertices + 1):
        if visited[i] == 0:
            queue = collections.deque([i])
            visited[i] = 1

            while queue:  
                node = queue.popleft()
                nodeTeam = visited[node]
                nextTeam = nodeTeam * -1

                for next in graph[node]:
                    if visited[next] == 0:
                        visited[next] = nextTeam
                        queue.append(next)
                    elif visited[next] == nodeTeam:
                        return "NO"
    return "YES"

testcase = int(input())

for _ in range(testcase):

    answer = "YES"

    vertice, edge = map(int, input().split())

    graph = [[] for _ in range(vertice + 1)]

    for i in range(edge):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    print(BFS(graph, vertice))
