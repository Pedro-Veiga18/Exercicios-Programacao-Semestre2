from random import randint



#Função para gerar matriz
def gerar_matriz():
    A = [[randint(1, 5)for j in range(2)] for i in range(3)]
    B = [[randint(1, 5)for j in range(3)] for i in range(2)]
    return A, B
    

#Função para imprimir matriz   
def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()
        
#Função para multiplicar as matrizes
def multiplicar_matriz(A, B):
    C = []
    for i in range(len(A)):
        linha = []
        for j in range(len(B[0])):
            aux = 0
            for k in range(len(A[i])):
                aux += A[i][k] * B[k][j]
            linha.append(aux)
        C.append(linha)
    return C
    


#Função principal
def main():
    A, B = gerar_matriz()
    print(f"Matriz A:")
    imprimir_matriz(A)
    print()
    print(f"Matriz B:")
    imprimir_matriz(B)
    C = multiplicar_matriz(A, B)
    print()
    print(f"Matriz C:")
    imprimir_matriz(C)


#Programa principal
if __name__ == '__main__':
    main()