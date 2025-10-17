from random import randint

def gerar_matriz():
    ordem = randint(2, 5)
    matriz = [[randint(0, 10)for j in range(ordem)] for i in range(ordem)]
    return matriz



def imprimir(matriz):
    ordem = len(matriz)
    for i in range(ordem):
        for j in range(ordem):
            print(matriz[i][j], end='\t')
        print()
        
def trocar(matriz):
    j = len(matriz) - 1
    for i in range(len(matriz)):
        aux = matriz[i][i]
        matriz[i][i] = matriz[i][j]
        matriz [i][j] = aux
        j -= 1
    
    
#Programa principal
matriz = gerar_matriz()
print("Impressão antes da troca")
imprimir(matriz)
trocar(matriz)
print("\n Impressão após a troca")
imprimir(matriz)
