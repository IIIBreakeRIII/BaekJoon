# No.2606 바이러스

import sys
import collections

input = sys.stdin.readline

computer_count = int(input())
network_count = int(input())

network_list = [[] for _ in range(computer_count + 1)]

for _ in range(network_count):
    a, b = map(int, input().split())
    network_list[a].append(b)
    network_list[b].append(a)

def bfs(graph, start):

    visited = [False] * (computer_count + 1)
    visited[start] = True
    
    queue = collections.deque([start])
    neighbor_count = 0

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                neighbor_count += 1
                queue.append(neighbor)

    return neighbor_count

print(bfs(network_list, 1))
