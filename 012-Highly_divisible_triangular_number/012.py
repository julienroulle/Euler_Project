import numpy as np

def divisors(n):
    possible_divisors = [i for i in range(1, int(np.sqrt(n)) + 1)]
    divisors = []

    for divisor in possible_divisors:
        if n % divisor == 0:
            divisors.extend((divisor, n//divisor))

    return len(divisors)

def triangle_number(n):
    return n*(n+1)//2

i = 0

while divisors(triangle_number(i)) < 500:
    i += 1

print(triangle_number(i))