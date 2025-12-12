class Sensor:
    def __init__(self, codigo : int, leitura : int):
        self.codigo = codigo
        self.leitura = leitura
        
        
        
def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = valor
        
        

def ordenacao(lista):
   
    leituras = []

    for sensor in lista:
        leituras.append(sensor.leitura)

    insercao(leituras)

    for leitura in leituras:
        for sensor in lista:
            if sensor.leitura == leitura:
                print(f"{sensor.codigo:<10}{sensor.leitura:<10}")
                break
        
        
        
def main():
    lista = []
    qnt = int(input("Quantidade de sensores: "))

    for i in range(qnt): 
        codigo = int(input("Codigo do sensor: "))
        leitura = int(input("Leitura do sensor: "))
        lista.append(Sensor(codigo, leitura))
        print('-' * 30) 
    
    print(f"{'Codigo':<10}{'Leitura':<10}")
    print('-' * 20)
        
    ordenacao(lista)
        
        
        
       
#Programa principal
if __name__ == '__main__':
    main()
    
    
#Bom natal e feliz ano novo professor!