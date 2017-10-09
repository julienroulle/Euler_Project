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

abundants = [i for i in range(1,28123) if i < sum_divisors(i)]

abundant_sum = [True for i in range(28123)]
for i in abundants:
    for j in abundants:
        if i + j <= 28123:
            abundant_sum[i+j-1] = False
        else:
            break

score = 0
for i, elt in enumerate(abundant_sum):
    if elt:
        score += i + 1

print(score)