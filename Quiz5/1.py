def estranho(A, x, l, r, depth=0):
    if l > r:
        return -1
    if depth % 2 == 0:
        if A[l] == x:
            return l
        if A[r] == x:
            return r
    else:
        if A[r] == x:
            return r
        if A[l] == x:
            return l
    return estranho(A, x, l-1, r-1, depth+1)



A = [9, 6, 8, 0, 7, 1, 5, 4, 2, 3, 10]

print(estranho(A, 4, 0, len(A)-1))

#4 chamadas