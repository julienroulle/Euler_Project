for i in range(1,1000):
    for j in range(1,1000-i+1):
        for k in range(1,1000-j-i+1):
            if i + j + k == 1000 and (i**2 + j**2 == k**2 or i**2 + k**2 == j**2 or j**2 + k**2 == i**2):
                print(i*j*k)
                exit(1)