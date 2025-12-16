class Emprestimo: 
    def __init__(self, Vl_Financiado = 0.0, Taxa_Juros = 0.0, Num_Parcela = 0, Id_Emprestimo = "", Nm_Cliente= ""):
        self.Vl_Financiado = Vl_Financiado
        self.Taxa_Juros = Taxa_Juros
        self.Num_Parcela = Num_Parcela
        self.Id_Emprestimo = Id_Emprestimo  
        self.Nm_Cliente = Nm_Cliente

    def ValorParcela(self) :
        financiamento = self.Vl_Financiado
        juros = self.Taxa_Juros
        parcelas = self.Num_Parcela

        if juros == 0 :
           calc =  financiamento / parcelas
           return calc
        else: 
          calc =  (financiamento * (juros/ (1 - ((1 + juros) ** (- parcelas)))))
        return calc

    def SaldoDevedor(self, k) :
    

        financiamento =   self.Vl_Financiado
        juros = self.Taxa_Juros
        parcela = self.ValorParcela()

        if juros == 0:
            return financiamento - (parcela * k)
        else:
            return (financiamento * ((1 + juros) ** k)) - (parcela * ((((1 + juros) ** k) - 1) / juros))        

    def jurosPagos(self) :
        qtd_parcela = self.Num_Parcela
        Vl_parcela = self.ValorParcela()
        Vl_Financiado = self.Vl_Financiado

        juros_pagos = (qtd_parcela * Vl_parcela) - Vl_Financiado
        return juros_pagos


def coletaDados() :

    financiamento_Vl = float(input('Digite o valor do Financiamento: '))

    taxa = float(input("Digite a taxa de juros (1.5 para 1,5%): "))
    taxa = taxa / 100

    parcelas_Num = int(input("Digite o numero de parcelas: "))

    id_Emprestimo = input("Digite o ID do emprestimo ")

    cliente = input("Digite o Nome do cliente: ")

    e = Emprestimo(financiamento_Vl,taxa, parcelas_Num, id_Emprestimo, cliente)

    return e


def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = valor


qtd_teste = int(input("Digite quantos testes quer fazer: "))

lista_emprestimo = []


for i in range(qtd_teste) :
    e = coletaDados()

    lista_emprestimo.append(e)



lista_juros = []

for e in lista_emprestimo:
    lista_juros.append(e.jurosPagos())
    
insercao(lista_juros)


print("[Ranking por juros totais]")

ranking = 1
for juros in lista_juros:
    for e in lista_emprestimo:
        if e.jurosPagos() == juros:
            parcela = e.ValorParcela()
            custo_total = parcela * e.Num_Parcela
            
            print(f"{ranking}) {e.Id_Emprestimo} - {e.Num_Parcela}x | Parcela: R$ {parcela:.2f} | Juros Totais: R$ {juros:.2f} | Custo Total: R$ {custo_total:.2f}")
            ranking += 1
            break


print("[Saldos após 12 parcelas]")
print("-" * 40)

k = 12
for e in lista_emprestimo:
    if k > e.Num_Parcela:
        saldo_devedor = 0
    else:
        saldo_devedor = e.SaldoDevedor(k)

    print(f"{e.Id_Emprestimo} - {e.Num_Parcela}x : R$ {saldo_devedor:.2f}")





