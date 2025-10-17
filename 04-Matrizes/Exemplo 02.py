
linha = int(input("Total de linhas: "))
coluna = int(input("Total de colunas: "))

m = [[int(input("Valor: ")) for j in range(coluna)] for i in range(linha)]

print(m)