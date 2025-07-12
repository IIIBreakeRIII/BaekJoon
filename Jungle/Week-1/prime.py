def find_n_primes(n):
    """
    n 이하의 모든 소수를 이중 for문만으로 찾아 리스트로 반환.
    O(n^2) 방식이므로 n이 커지면 실행 시간이 급격히 늘어납니다.
    """
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        # 2부터 num-1까지 모두 나눠본다
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes
