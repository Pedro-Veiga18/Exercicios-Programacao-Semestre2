lista = [0, 1, 0, 0, 1]
valor = 0
for j in range(len(lista)-1, -1, -1):
    valor = valor | lista[j] << (len(lista) - 1 - j)
    
    
print(valor)