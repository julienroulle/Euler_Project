import numpy as np 

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

limit = 600851475143
target = int(np.sqrt(600851475143)) + 1

target_primes = Eratosthenes_sieve(target)

for i in reversed(target_primes):
    if limit % i == 0:
        print(i)       
        exit(1)