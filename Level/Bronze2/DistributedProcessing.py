# No. 1009 분산 처리

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    if a == 10:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print((a * a) % 10)
        else:
            print(a % 10)
    else:
        b = b % 4
        if b == 0:
            print(a)
        elif b == 1:
            print((a ** 2) % 10)
