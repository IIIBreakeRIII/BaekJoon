def sieve_of_eratosthenes(n: int) -> list[int]:
    
    if n < 2:
        return []

    # Initialize a boolean array: True means "is prime"
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Only need to sieve up to sqrt(n)
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if is_prime[i]:
            # Mark multiples of i from i*i up to n as non-prime
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    print(is_prime)

    # Collect and return all primes
    return [i for i, prime in enumerate(is_prime) if prime]


# Example usage:
if __name__ == "__main__":
    n = 100
    primes_up_to_n = sieve_of_eratosthenes(n)
    print(f"Primes ≤ {n}:", primes_up_to_n)
