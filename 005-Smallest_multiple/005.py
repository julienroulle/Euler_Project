def is_evenly_divisible(n):
    divisors = [i for i in range(1,21)]

    for divisor in divisors:
        if n%divisor != 0:
            return False

    return True

cpt = 20

while not is_evenly_divisible(cpt):
    cpt += 20

print(cpt)