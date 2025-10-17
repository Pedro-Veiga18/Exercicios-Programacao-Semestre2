def filtro(leads):
    qualificados = []
    for i in range(len(leads)):
        if leads[i]["score"] >= 70:
            qualificados.append(leads[i])
    return qualificados

#Função para imprimir
def imprimir_leads_qual(qualificados):
    print(f"Qualificados:")
    for lead in qualificados:
        print(f"nome: {lead.get('nome')}", end=" ")
        print(f"origem: {lead.get('origem')}", end=" ")
        print(f"score: {lead.get('score')}", end=" ")
        print(f"status: {lead.get('status')}")
 
 #Funçao para fazer a taxa de conversao       
def taxa_conversao(leads: list[dict]):
    totais : dict[str, int] = {}
    ganho : dict[str, int] = {}
    
    for lead in leads:
        origem = lead.get("origem")
        status = lead.get("status")
        
        if origem not in totais:
            totais[origem] = 0
            ganho[origem] = 0
        
        totais[origem] += 1
        if status == "ganho":
            ganho[origem] += 1
            
     #calculo da taxa de conversao
    for origem in totais:
        t = totais.get(origem)
        g = ganho.get(origem)
        taxa = g / t if t > 0 else 0
        print(f"{origem} --> {(taxa*100): .2f}%")
   
         
     
    
#Função principal
def main():
    leads = [
    {"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},
    {"nome":"Beto","origem":"Google Ads","score":65,"status":"perdido"},
    {"nome":"Cris","origem":"Indicação","score":90,"status":"ganho"},
    {"nome":"Duda","origem":"Instagram","score":74,"status":"perdido"},
    {"nome":"Enzo","origem":"Google Ads","score":71,"status":"ganho"},
    ]
    
    qualificados = filtro(leads)
    imprimir_leads_qual(qualificados)
    taxa_conversao(leads)

    
    


  
#Programa principal
if __name__ == '__main__':
    main()