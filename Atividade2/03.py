#Dicionario de pedidos
pedidos = {
"P001": {"cliente": "Ana", "produtos": {"Mouse": 80.0, "Teclado": 120.0}},
"P002": {"cliente": "Bruno", "produtos": {"Monitor": 700.0}},
"P003": {"cliente": "Ana", "produtos": {"Cabo HDMI": 40.0, "Mouse": 80.0}},
"P004": {"cliente": "Carla", "produtos": {"Cadeira Gamer": 950.0}}
}

#a) Calcular o total gasto em cada pedido. Exemplo: {"P001": 200.0, "P002": 700.0, ...}.
total_gasto_pedido = {}
for pedido, chave in pedidos.items():
    total = sum(chave["produtos"].values())
    total_gasto_pedido[pedido] = total
print(f"O total gasto em cada pedido: {total_gasto_pedido}")

#b) Calcular o total gasto por cliente. Exemplo: {"Ana": 320.0, "Bruno": 700.0, "Carla": 950.0}.
total_gasto_cliente = {}
for chave in pedidos.values():
    cliente = chave["cliente"]
    total = sum(chave["produtos"].values())
    total_gasto_cliente[cliente] = total_gasto_cliente.get(cliente, 0) + total
print(f"O total gasto por cliente: {total_gasto_cliente}")

#c) Identificar o cliente que mais gastou.
cliente_mais_gastou = max((total, cliente) for cliente, total in total_gasto_cliente.items())[1]
print(f"O cliente que mais gastou foi: {cliente_mais_gastou}")

#d) Calcular e imprimir o faturamento total da loja.
fat_total = sum(sum(chave["produtos"].values()) for chave in pedidos.values())
print(f"O faturamento total da loja foi: {fat_total}")