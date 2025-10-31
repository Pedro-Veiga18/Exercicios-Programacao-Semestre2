"""
Implemente uma função em Python para comparar as notas de alguns alunos
na primeira prova e na segunda prova aplicada por um professor. A função deve
receber como parâmetro duas listas de tuplas, onde cada tupla contém o nome
de um aluno e sua nota em uma prova. A função deve exibir os seguintes
resultados:
a) Alunos que melhoraram suas notas da primeira prova para a segunda.
b) Alunos que pioraram suas notas.
c) Alunos que mantiveram a mesma nota.
"""




from random import random


def comparar(dict1: list, dict2: list):
    melhor = []
    pior = []
    igual = []
    
    for nome, valor in dict1.items():
        if valor < dict2.get(nome):
            melhor.append(nome)
        elif valor > dict2.get(nome):
            pior.append(nome)
        else:
            igual.append(nome)
    
    print(f"Os alunos que melhoraram: {melhor}")
    print(f"Os alunos que pioraram: {pior}")
    print(f"Os alunos que mantiveram: {igual}")
    
    return igual
    

def notas():
    p1 = []
    p1.append(("Veiga", round(random()*10,2)))
    p1.append(("Ricardao", round(random()*10,2)))
    p1.append(("Kevao", round(random()*10,2)))
    p1.append(("Knorre", round(random()*10,2)))
    p1.append(("Bulaxa", round(random()*10,2)))
    p1.append(("Rafarofas", round(random()*10,2)))
    
    return p1


#Função main()      
def main():
    p1 = notas()
    p2 = notas()
    dict1 = dict(p1)
    dict2 = dict(p2)       
    print(f"Notas da prova 1: {dict1}")
    print(f"Notas da prova 2: {dict2}")
    
    
        
#Programa Principal        
if __name__ == '__main__':
    main()