precos = {
    "arroz": 22.5,
    "feijao": 9.8,
    "leite": 4.7,
    "pao": 1.5
}
vendas = [
    ["arroz", "feijao", "feijao", "leite"],
    ["pao", "pao", "pao", "leite"],
    ["arroz", "leite"],
    ["feijao", "feijao", "feijao"]
]   

#a) Calcule o total de cada venda e armazene os resultados em uma lista chamada totais_venda.

def SomaVenda(vendas, precos) :
    totais_venda = []
    contador_vendas = 0
    for i in range(len(vendas)) :
        calc = 0
    
        for j in vendas[i] :
            calc = calc + precos[j]
            contador_vendas = contador_vendas +1
        totais_venda.append(calc)
    return totais_venda, contador_vendas

totais_venda,contador_vendas = SomaVenda(vendas, precos)

#b) Calcule o faturamento total (soma de todas as vendas).

def Faturamento(totais_venda) :
    faturamentoVl = 0
    for i in range(len(totais_venda)) :
       faturamentoVl= faturamentoVl +totais_venda[i]
    return faturamentoVl

valorFaturamento = Faturamento(totais_venda)

#c) Gere um dicionário qtd_por_item com a quantidade total vendida de cada produto.

def qtdVendida(vendas) : 
    qtd_por_item = {}
    for i in range(len(vendas)): 
        for j in vendas[i] :

            if j not in qtd_por_item :
                qtd_por_item[j] = 1
            else:
                qtd_por_item[j] += 1
    return qtd_por_item
    
qtd_por_item = qtdVendida(vendas)

#d) Identifique: o produto mais vendido (maior quantidade); o produto com maior faturamento individual (quantidade × preço).

def opercaoProduto(qtd_por_item) :
    nome_vendido = ''
    qtd_vendido = 0
    for chave, qtd in qtd_por_item.items():
        if qtd > qtd_vendido :
            qtd_vendido = qtd
            nome_vendido = chave
    mais_vendido = f"O item mais vendido é {nome_vendido}: {qtd_vendido} unidades."
    return mais_vendido

mais_vendido = opercaoProduto(qtd_por_item)

def faturaIndividual(qtd_por_item, precos) :
    maior_faturamento = 0
    produto_maior_fat = ''
    for chave,valor in qtd_por_item.items() :
        aux = 0
        aux = qtd_por_item[chave] * precos[chave]
        if aux > maior_faturamento :
            maior_faturamento = aux
            produto_maior_fat = chave
    mais_faturado = f"O produto com Maior faturamento é: {produto_maior_fat}: {maior_faturamento}"
    return mais_faturado

mais_faturado = faturaIndividual(qtd_por_item, precos)

#e) Calcule o ticket médio da loja (faturamento total ÷ número de vendas).

def ticket(contador_vendas, valorFaturamento) : 
    ticket_medio = valorFaturamento/contador_vendas
    return ticket_medio

ticket_medio = ticket(contador_vendas, valorFaturamento)

#f) Organize as informações em um dicionário relatorio com o formato:

relatorio = {
    "totais_venda": totais_venda,
    "faturamento_total": valorFaturamento,
    "qtd_por_item": qtd_por_item,
    "mais_vendido": mais_vendido,
    "mais_faturado": mais_faturado,
    "ticket_medio": ticket_medio
}

def exibirRelatorio(relatorio) :
    for chave, valor in relatorio.items():
        print(f'{chave} --> {valor}')
        print()

exibirRelatorio(relatorio)