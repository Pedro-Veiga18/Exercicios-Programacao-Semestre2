'''
programa exemplo para ler o RA, o nome e a nota dos alunos matriculados na disciplina
X. Em seguida, imprimir a quantidade de alunos aprovados (média maior ou igual a 7)
'''
lista = []

for i in range(2):
    ra = int(input("RA: "))
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    lista.append({'ra':ra, 'nome':nome, 'nota':nota})
  
'''
SOLUÇÃO INICIANTE
# quantidade de alunos que estão acima da média  
total = 0
for i in range(len(lista)):
    aluno = lista[i]
    if aluno['nota'] >= 7.0:
        total += 1

print(lista)
'''
#SOLUÇÃO ZIKA

total = 0
for aluno in lista:
    if aluno.get('nota') >= 7.0:
        total += 1

print(lista)