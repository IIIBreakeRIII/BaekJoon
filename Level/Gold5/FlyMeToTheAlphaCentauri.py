# No. 1011 Fly Me To The Alpha Centauri

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    n = y - x
    if n == 1:
        print(1)
    elif n == 2:
        print()
    elif n % 2 == 0:
        print(int(n / 2 + 1))
    else:
        print(int((n+1) / 2 + 1))
