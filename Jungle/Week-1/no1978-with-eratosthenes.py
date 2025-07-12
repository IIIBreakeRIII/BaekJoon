# No.1978 소수 찾기
# With using Eratosthenes

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1, 1):
        if num % i == 0:
            return False

    return True


def main():
    count = int(input())
    nums = list(map(int, input().split()))
    
    ans = 0

    for index in nums:
        if index == 1:
            continue
        elif is_prime(index) == True:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
