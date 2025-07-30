# No.2178 미로탐색

import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
maze_list = []

for i in range(n):
    maze_list.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):

    queue = collections.deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for index in range(4):
            nextX = x + dx[index]
            nextY = y + dy[index]

            if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m:
                continue
            if maze_list[nextX][nextY] == 1:
                queue.append((nextX, nextY))
                maze_list[nextX][nextY] = maze_list[x][y] + 1

    return maze_list[n - 1][m - 1]

print(BFS(0, 0))
