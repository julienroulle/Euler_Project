fibo = [1, 2]
sum = 2

while fibo[1] < 4*10**6:
    tmp = fibo[0] + fibo[1]
    fibo[0] = fibo[1]
    fibo[1] = tmp

    if tmp % 2 == 0:
        sum += tmp

print(sum)