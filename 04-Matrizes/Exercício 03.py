from random import randint

from math import inf

#Função das médias dos anos
def media_ano(matriz):
    media_lista =[]
    for i in range(10):
        temperaturas = 0
        for j in range(12):
            temperaturas += matriz[i][j]
        medias = temperaturas / 12
        media_lista.append(medias)
        print(f"Ano {i+1}: média = {medias:.2f}")
    return media_lista

#Função da maior e menor média dos anos
def maior_menor_ano(media_lista):
    ano_maior = media_lista.index(max(media_lista))
    ano_menor = media_lista.index(min(media_lista))       
    return ano_maior + 1, ano_menor + 1     


#Função main()
def main():
    #valores matriz
    matriz = [[randint(8, 40) for j in range(12)] for i in range(10)]
    #print(matriz)
    for i in matriz:
        for j in i:
            print(j, end="|")
        print()
    
    media_lista = media_ano(matriz)
    ano_maior, ano_menor = maior_menor_ano(media_lista)
    print(f"O ano com maior média é: {ano_maior}")
    print(f"O ano com menor média é: {ano_menor}")
 
 
    
#Programa principal
if __name__ == '__main__':
    main()



 

    

