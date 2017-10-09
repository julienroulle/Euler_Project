fibo = [1, 1]

i = 2
while fibo[1] < 10**999:
    tmp = fibo[0] + fibo[1]
    fibo[0] = fibo[1]
    fibo[1] = tmp
    i += 1

print(i)