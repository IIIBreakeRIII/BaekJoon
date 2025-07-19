# No.10830 행렬 제곱

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def matrix_expo(matrix, n, sub_matrix):

    result = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            for i in range(n):
                result[row][col] += matrix[row][i] * sub_matrix[i][col]
            result[row][col] %= 1000

    return result

def solution(matrix, n, b):
    if b == 1:
        return matrix
    elif b == 2:
        return matrix_expo(matrix, n, matrix)
    else:
        temp = solution(matrix, n, b // 2)

        if b % 2 == 0:
            return matrix_expo(temp, n, temp)
        else:
            return matrix_expo(matrix_expo(temp, n, temp), n, matrix)

result = solution(matrix, n, b)

for index in result:
    for num in index:
        print(num % 1000, end=' ')
    print()
