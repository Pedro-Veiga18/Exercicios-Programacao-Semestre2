def bubblesort(lista: list[int]) -> list[int]:
    for _ in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista
    
    
def selecao(x):
    n = len(x)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if x[j] < x[menor]:
                menor = j
                
        # Troca os elementos (essa linha precisa estar dentro do laço externo)
        x[i], x[menor] = x[menor], x[i]
        

#Função para ordenar uma lista pelo método de inserção
def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = valor
        

#Função para ordenar uma lista pelo método quicksort (pivô como último elemento)
def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    
    if inicio < fim:
        pivo = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivo -1)
        quicksort(lista, pivo + 1, fim)
        
def particionar(lista, inicio, fim) -> int: #Retorna o índice do pivô
    pivo = lista[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
            
    #Coloca o pivô no local correto
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1
        
        
    
    
    

    
