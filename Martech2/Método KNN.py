from math import sqrt


dados = [
    ('Priyanka', 3, 4, 4, 2, 4), 
    ('Justin', 4, 3, 5, 1, 5),
    ('Morpheus', 2, 5, 1, 3, 1)
]

genero = ['comedia', 'acao', 'drama', 'terror', 'romance']

#Função para calcular a distância entre dois usuários
def calcular_distancia(usuario: tuple, user_novo: tuple) -> float:
    soma = 0
    for i in range(1, len(usuario)):
        n1 = usuario[i]
        n2 = user_novo[i]
        if n1 is not None and n2 is not None:
            soma += (n1 - n2) ** 2
    return sqrt(soma)


#Função para encontrar o mais próximo
def mais_proximo(dados: list[tuple], user_novo: tuple) -> tuple:
    melhor_vizinho = None
    melhor_distancia = None
    for i in dados:
        distancia = calcular_distancia(i, user_novo)
        if (melhor_distancia is None) or (distancia < melhor_distancia):
            melhor_distancia = distancia
            melhor_vizinho = i[0]
    

#Função para fazer a recomendação
def recomendar(dados: list[tuple], user_novo: tuple) -> tuple:
    vizinho, distancia = mais_proximo(dados, user_novo)


#Função principal
def main():
    user_novo = ('Murphy', 3, 3, 3, 3, 3)
    vizinho, distancia = recomendar(dados, user_novo)



#Programa principal
if __name__ == '__main__':
    main()