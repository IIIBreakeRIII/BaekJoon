# No.9020 골드바흐의 추측

import sys
input = sys.stdin.readline

testcase = int(input())
testcase_list = []

# Erartosthenes
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1, 1):
        if num % i == 0:
            return False
        
    return True

def find_goldbach(num):
    half = num // 2
    prime_list = []
    answer = 0
    
    # append prime number before half of the num
    for i in range(half + 1):
        if is_prime(i):
            prime_list.append(i)
    
    # if {target num} - {biggest prime num} is prime num -> return
    for i in reversed(prime_list):
        if is_prime(num - i):
            answer = i
            break

    return answer


for t in range(testcase):
    testcase_list.append(int(input()))

for i in testcase_list:
    ans = find_goldbach(i)
    print(ans, i - ans)
