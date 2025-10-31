from random import randint

#b) Preencher a matriz com valores inteiros aleatórios (utilizar o módulo random). O preenchimento da matriz deverá ocorrer em uma função.
def gerar_matriz(n):
    return [[randint(1, 10) for j in range(n)] for i in range(n)]

#c) Imprimir a matriz em formato tabular (a impressão deverá ser ocorrer em uma função, diferente da função que fez o preenchimento).
def imprimir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end="\t")
        print()
    print()  

#d) Criar uma nova matriz do mesmo tamanho onde 'P' representa pico, 'V' representa vale e 'N' representa ponto neutro. A geração da matriz deverá ocorrer em uma função.
def classificar(matriz):
    n = len(matriz)
    direcoes = {
        "NO": (-1, -1), "N": (-1, 0), "NE": (-1, 1),
        "O":  ( 0, -1),               "L":  ( 0, 1),
        "SO": ( 1, -1), "S": ( 1, 0), "SE": ( 1, 1),
    }
    classificacoes = []
    for i in range(n):
        linha_clas = []
        for j in range(n):
            valor = matriz[i][j]
    
            viz = []
            for di, dj in direcoes.values():
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    viz.append(matriz[ni][nj])

        
            eh_pico = True
            k = 0
            while k < len(viz):
                if not (valor > viz[k]):
                    eh_pico = False
                    break
                k += 1

            if eh_pico:
                linha_clas.append('P')
            else:
               
                eh_vale = True
                k = 0
                while k < len(viz):
                    if not (valor < viz[k]):
                        eh_vale = False
                        break
                    k += 1
                if eh_vale:
                    linha_clas.append('V')
                else:
                    linha_clas.append('N')
        classificacoes.append(linha_clas)
    return classificacoes

#e) Imprima no terminal a nova matriz em formato tabular (a impressão deve ocorrer em uma função). 
def imprime_classificada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end="\t")
        print()
    print()

#a) Ler a ordem da matriz a partir do terminal.
def main():
    n = int(input("Informe a ordem da matriz: "))

    matriz = gerar_matriz(n)  
    print("\nMatriz de altitudes:")
    imprimir(matriz)

    classificacoes = classificar(matriz)
    print("Matriz de classificação (P=pico, V=vale, N=neutro):")
    imprime_classificada(classificacoes)

if __name__ == "__main__":
    main()
