a, b, c = map(int, input().split())

def recursion(a, b, c):

    if b == 1:
        return a % c

    result = recursion(a, b // 2, c)

    if b % 2 == 1:
        return ((result * result) % c) * a % c
    else:
        return (result * result) % c

print(recursion(a, b, c))
