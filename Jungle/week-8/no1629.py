# No.1629 곱셈

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def recursion(a, b, c):
    
    if b == 1:
        return a % c

    result = recursion(a, b // 2, c)
    
    if b % 2 == 0:      # Even Expo
        return (result * result) % c
    else:               # Odd Expo
        return ((result * result) % c) * a % c

print(recursion(a, b, c))
