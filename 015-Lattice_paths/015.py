import math

def permutation_number(k, n):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print(permutation_number(20, 40))