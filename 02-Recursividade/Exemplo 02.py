#Programa com função recursiva para ler um valor inteiro e positivo e retorne o
#valor de fibonnaci na posição indicada

def fibonnaci(p:int) -> int:
    if p == 1 or p == 2: return 1
    else:
        return fibonnaci(p-1) + fibonnaci(p-2)
    
#Função principal
def main():
    p = int(input("Informe um valor inteiro e positivo para a posição: "))
    if p <= 0:
        print("O valor deve ser inteiro e positivo.")
    else:
        print(f"{p}° posição da sequência de fibonnaci tem valor = {fibonnaci(p)}")
        
#Programa principal
if __name__ == "__main__":
    main()