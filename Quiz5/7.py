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





A = [2, 8, 7, 1, 3, 5, 6, 4]

print(quicksort(A))