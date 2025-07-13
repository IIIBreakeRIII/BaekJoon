# No.1074 Z

num, r, c = map(int, input().split())
size = 2 ** num

def dfs(row, col, n, ans):
    n = n // 2

    if row < n and col < n:
        if n == 1:
            print(ans)
            exit(0)
        dfs(row, col, n, ans)

    elif row < n and col >= n:
        if n == 1:
            print(ans+1)
            exit(0)
        dfs(row, col-n, n, ans + n**2)

    elif row >= n and col < n:
        if n == 1:
            print(ans+2)
            exit(0)
        dfs(row-n, col, n, ans + n**2 * 2)
    
    else:
        if n == 1:
            print(ans+3)
            exit(0)
        dfs(row-n, col-n, n, ans + n**2 * 3)

dfs(r, c, size, 0)
