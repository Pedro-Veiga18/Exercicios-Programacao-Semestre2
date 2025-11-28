from aluno import Aluno

lista = []

for i in range(3): 
    nome = input('Nome --> ')
    ra = int(input('RA --> '))
    nota1 = float(input('Nota 1 --> '))
    nota2 = float(input('Nota 2 --> '))
    lista.append(Aluno(nome, ra, nota1, nota2))
    print('-' * 30)

# impressão do nome, da média e da situação
print(f"{'Nome':<20}{'Média':<10}{'Situação'}")
print('-' * 40)
for alunos in lista:
    media = alunos.calcular_media()
    print(f'{alunos.nome :<20}{media:<10.2f}{alunos.situacao()}')



