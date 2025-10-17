#Movimentações
def movimentacoes(estoque, movimentacao):
    for mov in movimentacao:
        produto = mov[0]
        quant = mov[1]
        
        if produto not in estoque:
            estoque[produto] = {"saldo": quant, "min": 0, "preco": 0}
        else:    
            estoque[produto]["saldo"] += quant
        
#Função para imprimir
def imprimir_estoque(estoque):
    print("Estoque:")
    for produto, dados in estoque.items():  
        print(f"{produto}: ", end="")
        print(f"saldo: {dados.get('saldo')}", end=" ")
        print(f"mínimo: {dados.get('min')}", end=" ")
        print(f"preço: R${dados.get('preco'):.2f}")

#Função principal
def main():
    estoque = {
    "café": {"saldo": 10, "min": 12, "preco": 12.50},
    "pão": {"saldo": 30, "min": 25, "preco": 2.00},
    "queijo": {"saldo": 5, "min": 12, "preco": 34.00},
    }
    movimentacao = [
    ["café", -3],
    ["pão", -10],
    ["café", 5],
    ["leite", 8] # produto novo não cadastrado
    ]
    
    movimentacoes(estoque, movimentacao)
    imprimir_estoque(estoque)
    


#Programa principal
if __name__ == '__main__':
    main()
    