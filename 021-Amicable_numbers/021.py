import numpy as np

def sum_divisors(n):
    possible_divisors = [i for i in range(2, int(np.sqrt(n)) + 1)]
    divisors = [1]

    for divisor in possible_divisors:
        if n % divisor == 0:
            if divisor != n//divisor:
                divisors.extend((divisor, n//divisor))
            else:
                divisors.append(divisor)

    return sum(divisors)

amicable_sum = 0

for i in range(1,10**4):
    tmp_sum = sum_divisors(i)
    
    if sum_divisors(tmp_sum) == i and tmp_sum != i:
        amicable_sum += i

print(amicable_sum)