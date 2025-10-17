#Função multiplicação pela soma

def mult(m: int, n: int) -> int:
    if n == 0: return 0
    if n > 0: return m + mult(m, n-1)
    return -mult(m, -n)
    


#Função principal
def main():
    m = int(input("Informe o primeiro valor: "))
    n = int(input("Informe o segundo valor: "))
    print(f"{m} * {n} = {mult(m,n)}")
    


#Programa principal
if __name__ == "__main__":
    main()