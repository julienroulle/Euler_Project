from operator import add
from functools import reduce

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

primes = Eratosthenes_sieve(2*10**6)

print(reduce(add, primes))