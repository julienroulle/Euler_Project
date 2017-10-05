def Eratosthenes_sieve(limit):
    is_prime = [True for i in range(limit)]
    primes = []

    is_prime[0], is_prime[1] = False, False

    for i, isPrime in enumerate(is_prime):
        if isPrime:
            for j in range(i*i, limit, i):
                is_prime[j] = False
            primes.append(i)

    return primes

target = 10**4
primes = []
i = 2

while len(primes) < target:
    primes = Eratosthenes_sieve(i)
    i *= 2
    
print(Eratosthenes_sieve(10**6)[target])