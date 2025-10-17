#Função pra cálculo
def potencia(x:int,n:int) -> int:
    if n == 0: return 1
    else:
        return x * potencia(x,n-1)
    
    
#Função principal
def main():
    x = int(input("Digite um valor para x: "))
    n = int(input("Digite um valor inteiro e positivo: "))
    if n < 0:
        print("O valor deve ser inteiro, positivo.")
    else:
        print(f"O valor {x} elevado a {n} é = {potencia(x,n)}")
        
#Programa principal
if __name__ == "__main__":
    main()