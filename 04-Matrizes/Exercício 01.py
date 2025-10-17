from random import randint

lista = []
lista_nova = []

#Lendo os valores para a lista original
for i in range(randint(2, 8)):
    lista.append(randint(-2, 10))
    if lista[i] not in lista_nova:
        lista_nova.append(lista[i])
        
print(f"Lista original: {lista}")
print(f"Lista nova: {lista_nova}")