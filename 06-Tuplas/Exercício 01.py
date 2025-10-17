from random import randint
from math import sqrt


#Função para gerar a lista de pontos
def gerar_pontos():
    lista = []    
    for _ in range(randint(1, 5)):
        lista.append((randint(-10, 10), randint(-10, 10)))
    return lista        


#Função para calcular a distância de cada um dos pontos até a origem
def calcular_distancia(lista):
    distancia = []
    for i in range(len(lista)):
        x, y = lista[i]
        distancia.append(sqrt(x * x + y * y))
    return distancia


#Função para retornar o ponto mais distante da origem
def maisDistante(lista, distancia):
    ponto = lista[0]
    maior = distancia[0]
    for i in range(len(lista)):
        if distancia[i] > maior:
            maior = distancia[i]
            ponto = lista[i]
    return ponto


#Função para retornar o ponto mais próximo da origem
def maisProximo(lista, distancia):
    ponto = lista[0]
    menor = distancia[0]
    for i in range(len(lista)):
        if distancia[i] < menor:
            menor = distancia[i]
            ponto = lista[i]
    return ponto
    

#Função para calcular a média das distâncias
def calcularMedia(distancia):
    media = 0
    for d in distancia:
        media += d
    return media / len(distancia)

     
#Função main()      
def main():
    lista = gerar_pontos()
    distancia = calcular_distancia(lista)
    for i in range(len(lista)):
        print(f"{lista[i]} --> {distancia[i]:.2f}")
        
    print(f"ponto mais distante me relação a origem --> {maisDistante(lista, distancia)}")
    print(f"ponto mais próximo me relação a origem --> {maisProximo(lista, distancia)}")
    print(f"média das distâncias --> {calcularMedia(distancia):.2f}")
    
        
#Programa Principal        
if __name__ == '__main__':
    main()