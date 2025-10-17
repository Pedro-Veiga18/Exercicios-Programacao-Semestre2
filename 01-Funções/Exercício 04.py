#Função para gerar números primos
def gerar_primos(n:int) -> bool:
    lista = []
    valor = 2
    while len(lista) < n:
        if eh_primo(valor):
            lista.append(valor)
        valor = valor + 1
    return lista

#Função main
def main() -> None:
    n = int(input("Informe a quantidade de números primos: "))
    lista = gerar_primos(n)
    imprimir(lista)
    
#Programa principal
if __name__ == "__main__":
    main()