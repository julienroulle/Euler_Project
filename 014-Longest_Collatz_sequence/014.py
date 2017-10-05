def Collatz_sequence(n):
    seq = [n]

    while n > 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1

        seq.append(n)

    return seq


longest_sequence = 0
number = 0

for i in range(10**6):
    seq = Collatz_sequence(i)
    
    if len(seq) > longest_sequence:
        longest_sequence = len(seq)
        number = i

print(longest_sequence, number)