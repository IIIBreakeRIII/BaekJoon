def Check(depth):
    for i in range(depth):
        if board[depth] == board[i] or abs(board[depth] - board[i]) == depth - i:
            return False
    return True

def DFS(depth):
    global result

    if depth == N:
        result += 1
        return

    for i in range(N):
        board[depth] = i
        if Check(depth):
            DFS(depth + 1)


N = int(input())
board = [0 for i in range(N)]
result = 0

DFS(0)
print(result)
