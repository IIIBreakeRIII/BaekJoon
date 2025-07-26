# No.1916 최소비용 구하기

import heapq

cities = int(input())
buses = int(input())
buses_list = [[] for _ in range(cities + 1)]

# list-index로 출발지, 목적지, 비용을 입력
for _ in range(buses):
    dep, arr, cost = map(int, input().split())
    buses_list[dep].append((arr, cost))

# 구하고자하는 출발지 to 도착지
departure, arrival = map(int, input().split())

# 거리 설정 (초기값 INF)
distances = [float("INF")] * (cities + 1)

def dijkstra(graph, start):
    # 처음 방문하는 곳 0
    distances[start] = 0
    # 큐에 입력
    queue = [(start, 0)]
    
    # 큐 안에 추적하는 노드들이 있으면
    while queue:
        current_node, current_distance = heapq.heappop(queue)
        
        # 현재 거리가 distances 안의 같은 인덱스의 거리보다 길면 패스
        if current_distance > distances[current_node]:
            continue
        # 그래프 현재 노드의 인접 노드를 확인
        for neighbor, weight in graph[current_node]:
            # 현재 경로를 통해 이웃 도시로 가는 비용 계산
            distance = current_distance + weight
            #  짧으면 distances 최신화 후 큐 삽입
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (neighbor, distance))

    return distances

dijkstra(buses_list, departure)
print(distances[arrival])
