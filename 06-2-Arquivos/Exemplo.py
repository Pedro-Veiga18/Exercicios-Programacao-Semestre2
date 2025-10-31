#Bloco de leitura de arquivo
quant_aprov = 0
with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        nome, nota1, nota2 = linha.split(";")
        print(nome)
        print(nota1)
        print(nota2)
        
        if (float(nota1) + float(nota2)) >= 14:
            quant_aprov += 1
    
    print(f"A quantidade de aprovados foi: {quant_aprov}")