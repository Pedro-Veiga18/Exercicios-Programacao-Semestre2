def ordena(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] >= x:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = x
    return A


A =  [56, 34, 12, 7, 89, 90, 5]

print(ordena(A))