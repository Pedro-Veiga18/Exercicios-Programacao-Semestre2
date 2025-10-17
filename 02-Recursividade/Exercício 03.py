#Funçáo mdc --> para calcular e retornar o máximo divisor comum
def mdc(m: int, n: int) -> int:
    if n > m:
        return mdc(n,m)
    elif n == 0:
        return m
    return mdc(n, m % n)

#Função principal
def main():
    m = int(input("Informe o valor de m: "))
    n = int(input("Informe o valor de n: "))
    print(f"mdc({m},{n}) = {mdc(m,n)}")


#Programa principal
if __name__ == "__main__":
    main()