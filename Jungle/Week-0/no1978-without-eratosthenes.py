# 1978번 소수 찾기

# Code without using Eratosthenes

import sys

count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def is_prime(num):
    if num < 2:
        return False
    
    for index_value in range(2, int(num ** 0.5) + 1, 1):

        if num % index_value == 0:
            return False
        else:
            continue

ans = 0

for index in nums:
    if is_prime(index) == False:
        pass
    else:
        ans += 1

print(ans)
