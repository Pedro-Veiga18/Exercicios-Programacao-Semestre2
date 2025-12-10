def bubblesort(lista: list[int]) -> list[int]:
    for _ in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista


A = [64, 34, 25, 12, 22, 11, 90]

print(bubblesort(A))