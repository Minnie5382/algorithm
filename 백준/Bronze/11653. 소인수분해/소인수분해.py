def get_prime_factors(N):
    prime_factors = []
    for divisor in range(2, int(N ** 0.5) + 1):
        while N % divisor == 0:
            prime_factors.append(divisor)
            N //= divisor

    if N != 1:
        prime_factors.append(N)

    return prime_factors

N = int(input())
for f in get_prime_factors(N):
    print(f)