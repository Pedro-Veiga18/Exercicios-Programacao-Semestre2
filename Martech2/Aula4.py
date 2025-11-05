#função para calcular o tamanho da maior subsequência
def calcular_tamanho(palavra1: str, palavra2: str) -> int:
    tabela = [[0] * (len(palavra2) + 1) for _ in range(len(palavra1) + 1)] 
    for i in range(1, len(palavra1) + 1):
        for j in range(1, len(palavra2) + 1):
            if palavra1[i - 1] == palavra2[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1])
    return tabela[len(palavra1)][len(palavra2)]
            


#função principal
def main():
    palavra1 = input("Primeira palavra: ")
    palavra2 = input("Segunda palavra: ")
    tamanho = calcular_tamanho(palavra1, palavra2)
    print(f"Tamanho da maior subsequência {tamanho}")


#programa principal
if __name__ == '__main__':
    main()