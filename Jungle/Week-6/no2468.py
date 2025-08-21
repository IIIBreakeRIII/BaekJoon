# No.2468 안전 영역

import sys
input = sys.stdin.readline

n = int(input())
geo_info = []

for _ in range(n):
    geo_info.append(list(map(int, input().split())))

# moving coordinate
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# definite dfs
def dfs(x, y, height, visited):
    visited[x][y] = True
    
    # find tblr
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # not visited, in the range, if not flooded
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and geo_info[nx][ny] > height:
                dfs(nx, ny, height, visited)

# highest level of geo_info
flood_level= max(map(max, geo_info))

result = 0

# 0 to highest level of geo_info
for h in range(0, flood_level + 1):

    # initialize visited list
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and geo_info[i][j] > h:
                dfs(i, j, h, visited)
                count += 1
    result = max(result, count)

print(result)
