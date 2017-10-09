def permutation(lst):
 
    if len(lst) == 0:
        return []
 
    if len(lst) == 1:
        return [lst]
 
    l = [] 
 
    for i in range(len(lst)):
       m = lst[i]

       remLst = lst[:i] + lst[i+1:]
 
       for p in permutation(remLst):
           l.append([m] + p)
    return l

l = [i for i in range(10)]

print(permutation(l)[10**6 - 1])