# No.21606 아침 산책

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

vertices = int(input())
vertices_color = input().rstrip()

graph = [[] for _ in range(vertices + 1)]
visited = [0] * (vertices + 1)

# 실내 / 실외
place = [0] * (vertices + 1)

for i in range(len(vertices_color)):
    if vertices_color[i] == "1":
        place[i + 1] = 1

for _ in range(vertices - 1):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    result = 0

    for next_node in graph[node]:
        if place[next_node] == 0:
            if not visited[next_node]:
                visited[next_node] = 1
                result += dfs(next_node)
        else:
            result += 1
    return result

answer = 0

for i in range(1, vertices + 1):
    if place[i] == 0:
        if not visited[i]:
            visited[i] = 1
            result = dfs(i)
            answer += result * (result - 1)
    else:
        for next_node in graph[i]:
            if place[next_node] == 1:
                answer += 1

print(answer)
