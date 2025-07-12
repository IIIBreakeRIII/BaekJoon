# No.9020 골드바흐의 추측

testcase = int(input())
testcase_list = []

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1, 1):
        if num % i == 0:
            return False
    
    return True

def find_goldbach(num):
    half_num = num // 2
    prime_list = []
    ans = 0

    for i in range(half_num + 1):
        if is_prime(i):
            prime_list.append(i)

    for i in reversed(prime_list):
        if is_prime(num - i):
            ans = i
            break
    
    return ans

for t in range(testcase):
    testcase_list.append(int(input()))

for index in testcase_list:
    ans = find_goldbach(index)
    print(ans, index - ans)
