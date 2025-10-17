#Função para calcular total de grãos
def calcular() -> int:
    total = 0
    for i in range(65):
        total += 2 ** i
    return total

#Programa principal
total = calcular()
print(f"Total de grãos: {total}")
print()