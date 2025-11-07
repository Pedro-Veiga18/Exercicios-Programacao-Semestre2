

def engracada(risada: str) -> bool:
    vogais = []
    vogais_inv = []
    risada = risada.lower()
    risada_inv = risada[::-1]
    
    for i in range(len(risada)):
        if risada[i] == "a":
            vogais.append(risada[i])
        elif risada[i] == "e":
            vogais.append(risada[i])
        elif risada[i] == "i":
            vogais.append(risada[i])
        elif risada[i] == "o":
            vogais.append(risada[i])
        elif risada[i] == "u":
            vogais.append(risada[i])
            
    
    for _ in range(len(risada_inv)):
        if risada_inv[_] == "a":
            vogais_inv.append(risada_inv[_])
        elif risada_inv[_] == "e":
            vogais_inv.append(risada_inv[_])
        elif risada_inv[_] == "i":
            vogais_inv.append(risada_inv[_])
        elif risada_inv[_] == "o":
            vogais_inv.append(risada_inv[_])
        elif risada_inv[_] == "u":
            vogais_inv.append(risada_inv[_])
            
            
    
    print(f"Ordem normal de vogais: {vogais}")
    print(f"Ordem invertida de vogais: {vogais_inv}")
    if vogais == vogais_inv:
        return True
    else:
        return False
        
        
        
       
   




def main():
    risada = str(input("Digite a sua risada: "))
    gostou = engracada(risada)
    
    print(risada)
    if gostou == True:
        print(f"Valentina gostou")
    elif gostou == False:
        print(f"Valentina não gostou")
        










#Programa principal
if __name__ == '__main__':
    main()
    