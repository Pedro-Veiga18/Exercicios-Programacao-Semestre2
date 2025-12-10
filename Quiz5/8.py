def estranho(A):
    if len(A) <= 1:
        return A
    
    p = A[0]
    L = [x for x in A[1:] if x < p]
    E = [x for x in A if x == p]
    G = [x for x in A[1:] if x > p]
    return estranho(G) + E + estranho(L)

A = [17, 18, 90, 5, 76, 3, 2, 15]

print(estranho(A))