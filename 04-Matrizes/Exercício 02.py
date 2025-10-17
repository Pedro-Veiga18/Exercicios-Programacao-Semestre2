from random import randint

dp = 0
ds = 0



#Lendo os valores da matriz
matriz = [[randint(1, 10) for j in range(4)] for i in range(4)]
#print(matriz)
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end="\t")
    print()

#Soma dos elementos da diagonal principal e da secundária
for i in range(len(matriz)):
    for j in range(len(matriz)):
        #Verifica se o elemento está na diagonal principal
        if i == j:
            dp += matriz[i][j]
        #Verifica se o elemento está na diagonal secundária
        if i + j == len(matriz) -1:
            ds += matriz[i][j]
            
print(f"Soma dos elementos da diagonal principal {dp}")
print(f"Soma dos elementos da diagonal secundária: {ds}")