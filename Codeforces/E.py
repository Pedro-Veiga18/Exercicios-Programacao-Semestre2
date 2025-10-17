def rotacao(mat, n):
    nova_mat = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova_mat[n-j-1][i] = mat[i][j]
    return nova_mat

def ordenado(mat, n):
    for i in range(n):
        for j in range(n-1):
            if mat[i][j] >= mat[i][j+1]:
                return False
            if mat[j][i] >= mat[j+1][i]:
                return False
    return True

n = int(input())
mat = []
for _ in range(n):
    linha = [int(x) for x in input().split()]
    mat.append(linha)

for r in range(4):
    if ordenado(mat, n):
        print(r)
        break
    mat = rotacao(mat, n)