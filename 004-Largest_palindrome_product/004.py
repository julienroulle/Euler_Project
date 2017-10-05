def is_palindrome(nb):
    return str(nb) == str(nb)[::-1]

max_palindrome = 0

for i in range(1000,1,-1):
    for j in range(1000,1,-1):
        if is_palindrome(i*j) and i*j > max_palindrome:
            max_palindrome = i*j

print(max_palindrome)
            