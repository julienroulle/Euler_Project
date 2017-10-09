def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

target = str(factorial(100))
sum = 0

for digit in target:
    sum += int(digit)

print(sum)