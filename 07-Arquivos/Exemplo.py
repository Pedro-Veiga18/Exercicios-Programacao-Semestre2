#Bloco de leitura de arquivo
with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        nome, nota1, nota2 = linha.split(".")
        print(nome)
        print(nota1)
        print(nota2)