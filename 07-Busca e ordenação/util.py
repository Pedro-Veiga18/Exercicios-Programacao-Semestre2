def bubblesort(lista: list[int]) -> list[int]:
    for _ in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista
    
    
    
    
    

    
