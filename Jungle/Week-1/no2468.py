# No.2468 안전 영역

import sys
sys.setrecursionlimit(10001)  # 재귀 깊이 제한 증가

# 입력
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 이동 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# DFS 정의
def dfs(x, y, height, visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and cities[nx][ny] > height:
                dfs(nx, ny, height, visited)

# 전체 높이 중 최대값 계산
flood_level= max(map(max, cities))

# 결과값 저장용 변수
result = 0

# 각 비의 높이에 대해 시뮬레이션
for h in range(0, flood_level + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and cities[i][j] > h:
                dfs(i, j, h, visited)
                count += 1
    result = max(result, count)

print(result)
