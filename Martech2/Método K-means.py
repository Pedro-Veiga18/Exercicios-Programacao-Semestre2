import random
ponto = list[float]

def kmeans(dados: list[ponto], k: int = 3, max_iter: int = 200, tolerancia: float = 1e-6):
    n = len(dados) # tamanho da lista
    dimensao = len(dados[0]) #número de elementos em cada lista
    
    indices = list(range(n))
    random.shuffle(indices)
    
    centros = [dados[indices[i]][:] for i in range(k)]
    
    it = 1
    while it <= max_iter:
        for i in range(n):
            dado = dados[i]
            menor_distancia = float('inf')
            for j in range(k):
                dist = distancia(dado, centros[j])
                if dist < menor_distancia:
                    menor_distancia = dist



def main():
    dados = [ [1.0, 1.0], [1.2, 0.9], [0.9, 1.1], # grupo A
             [4.0, 4.2], [3.9, 3.5], [4.1, 3.8], # grupo B
             [8.0, 8.0], [8.3, 7.9], [7.7, 8.2] # grupo C
        
    ]
    
    kmeans(dados, k = 3, max_iter = 200, tolerancia = 1e-6)





if __name__ == '__main__':
    main()