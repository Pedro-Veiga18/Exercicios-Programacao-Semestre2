#Valores
import random
i = random.randint(1, 5) / 100
print(f"A taxa de juros é de {i*100: .2f}%")
n = 12


#Leitura de arquivo
with open("clientes.txt", "r", encoding="utf-8") as tabela:
    for linha in tabela:
        linha = linha.strip()
        if linha == "":
            continue
        
        nome, valor_finan = linha.split(";")
        
        pmt = float(valor_finan) * ((i * (i + 1) ** n) / ((i + 1) ** n - 1))
        
                
        print(f"Cliente: {nome}, Valor Financiado: {float(valor_finan):.2f}, Valor Parcela: {pmt:.2f}")