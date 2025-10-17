from random import randint

#Função contar
def contar(matriz):
    n = len(matriz)
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            contador = 0
            for k in range(n):
                if matriz[i][k] == 1 and matriz[j][k] == 1:
                    contador += 1
                    
            total += contador * (contador-1) // 2

    return total



#Dados
n = int(input("Digite o tamanho da matriz quadrada: "))
contador = 0


#Lendo os valores da matriz
matriz = [[randint(0, 1) for j in range(n)] for i in range(n)]
#print(matriz)
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end="\t")
    print()
    
print({contar(matriz)})
    
            
            
    

