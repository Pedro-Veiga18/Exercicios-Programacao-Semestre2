from random import randint

#a) Gerar um labirinto de caracteres. A ordem da matriz que representará o labirinto deverá ser
#informada pelo terminal. A geração do labirinto deverá ser realizada em uma função. Veja a
#seguir um exemplo de labirinto (a entrada e saída não precisam estar necessariamente nas
#bordas da matriz).

def gerar_labirinto(n):
    prob_parede = randint(10, 80)
    lab = []
    i = 0
    while i < n:
        linha = []
        j = 0
        while j < n:
            if randint(1, 100) <= prob_parede:
                linha.append('#')
            else:
                linha.append('.')
            j = j + 1
        lab.append(linha)
        i = i + 1

    ei = randint(0, n - 1)
    ej = randint(0, n - 1)
    si = randint(0, n - 1)
    sj = randint(0, n - 1)
    while si == ei and sj == ej:
        si = randint(0, n - 1)
        sj = randint(0, n - 1)

    lab[ei][ej] = 'E'
    lab[si][sj] = 'S'
    return lab


def imprimir(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j], end="\t")
        print()
    print()


def achar_ES(lab):
    n = len(lab)
    ei = -1; ej = -1; si = -1; sj = -1
    i = 0
    while i < n:
        j = 0
        while j < n:
            if lab[i][j] == 'E':
                ei = i; ej = j
            elif lab[i][j] == 'S':
                si = i; sj = j
            j = j + 1
        i = i + 1
    return (ei, ej), (si, sj)

#b) Uma função deverá verificar se existe ou não um caminho de 'E' até 'S'. A função deverá
#retornar um valor booleano. No caso do labirinto mostrado no exemplo acima não há um
#caminho entre 'E' e 'S'.

def existe_caminho(lab):
    n = len(lab)
    (ei, ej), (si, sj) = achar_ES(lab)

    
    if ei == -1 or si == -1:
        return False

    
    ja_viu = []
    i = 0
    while i < n:
        linha = []
        j = 0
        while j < n:
            linha.append(False)
            j = j + 1
        ja_viu.append(linha)
        i = i + 1

    
    movimentos = {
        "cima":    (-1, 0),
        "baixo":  ( 1, 0),
        "esquerda":  ( 0,-1),
        "direita": ( 0, 1),
    }

    
    ainda_nao_viu = []
    ainda_nao_viu.append((ei, ej))
    ja_viu[ei][ej] = True

    while len(ainda_nao_viu) > 0:
        i, j = ainda_nao_viu.pop(0)  

        if i == si and j == sj:
            return True

        
        for passo in movimentos.values():
            di = passo[0]
            dj = passo[1]
            ni = i + di
            nj = j + dj

            
            if ni >= 0 and ni < n and nj >= 0 and nj < n:
                if lab[ni][nj] != '#':
                    if ja_viu[ni][nj] == False:
                        ja_viu[ni][nj] = True
                        ainda_nao_viu.append((ni, nj))

    return False



#Função main
def main():
    n = int(input("Informe a ordem da matriz: "))
    lab = gerar_labirinto(n)

    print("\nLabirinto:")
    imprimir(lab)

    achou = existe_caminho(lab)
    if achou:
        print("Existe caminho de 'E' até 'S'.")
    else:
        print("Não existe caminho de 'E' até 'S'.")


#Programa principal
if __name__ == "__main__":
    main()
