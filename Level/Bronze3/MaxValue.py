# No. 2566 최댓값

import sys

Board = []

for _ in range(9):
	Board.append(list(map(int, sys.stdin.readline().split())))

a = 0
b = 0
max = 0

for i in range(9):
	for j in range(9):
		if max <= Board[i][j]:
			max = Board[i][j]
			a = i + 1
			b = j + 1

print(max)
print(a, b)
