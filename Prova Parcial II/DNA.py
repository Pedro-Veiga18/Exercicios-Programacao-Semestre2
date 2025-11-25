

#a)
def ler_dnas(dnas: list) -> list:
    tamanho_valido = []
    tamanho_invalido = []
    for dna in dnas:
        if len(dna.get("pai")) == len(dna.get("filho")):
            if len(dna.get("pai")) >= 2:
                tamanho_valido.append(dna)
            else:
                tamanho_invalido.append(dna)
        else:
            tamanho_invalido.append(dna)
            
    return tamanho_valido, tamanho_invalido

#b)
def compativel_dnas(tamanho_valido, tamanho_invalido):
    metades_pai = []
    metades_filho = []
    for i in range(len(tamanho_valido)):
        metade_num = len(tamanho_valido[i]["pai"]) // 2
        
        metades_pai.append(tamanho_valido[i]["pai"][metade_num:])
    
    for _ in range(len(tamanho_valido)):
        metade_num2 = len(tamanho_valido[_]["filho"]) // 2
        
        metades_filho.append(tamanho_valido[_]["filho"][metade_num2:])
        
        
      
    for j in range(len(metades_pai)):
        porcento = porcentagem(metades_pai[j], metades_filho[j])
        if porcento == True:
            print(f"POTENCIAL PAI-FILHO")
        elif porcento == False:
            print(f"NÃO COMPATÍVEL")
            
    for w in range(len(tamanho_invalido)):
        dna_ruim = tamanho_invalido[0]
        if dna_ruim == tamanho_invalido[w]:
            print(f"SEQUÊNCIAS DE TAMANHO INVÁLIDO")

        
        
def porcentagem(metades_pai: list, metades_filho: list) -> bool:
    for j in range(len(metades_pai)):
        igual_dna = []
        for k in range(len(metades_pai[j])):
            if metades_pai[j][k] == metades_filho[j][k]:
                igual_dna.append(metades_pai[j][k])
                
        tamanho_total = len(metades_pai[j])
        tamanho_igual = len(igual_dna)
        porcentagem_igual = ((tamanho_igual) / (tamanho_total)) * 100
        
        if porcentagem_igual >= 70:
            return True
        else: 
            return False
          
   


def main():
    dnas = [
        {"pai": "ACGTACGTACGTACG", "filho": "ACGTACGTACGAACG"},
        {"pai": "ACGTACGTACGTACG", "filho": "ACGTACGTACACACG"},
        {"pai": "AGCTA", "filho": "AGGTC"},
        {"pai": "ACGTACGT", "filho": "ACGTACGA"},
        {"pai": "ACGTACGT", "filho": "ACGTTCGA"},
        {"pai": "ACGTACGTACGTACG", "filho": "ACGTACGTACGTA"}
    ]
    tamanho_valido, tamanho_invalido = ler_dnas(dnas)
   
    compativel_dnas(tamanho_valido, tamanho_invalido)
    
    
    
        












#Programa principal
if __name__ == '__main__':
    main()
    