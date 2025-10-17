#Função Filtro
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
def taxa_conversao(leads):
    num_total_origem = {}
    num_ganhos_origem = {}
    tax = {}
    for lead in leads:
        origem = lead["origem"]
        status = lead["status"]
        
        num_total_origem[origem] =  num_total_origem.get(origem, 0) + 1
        
        if status == "ganho":
            num_ganhos_origem[origem] = num_ganhos_origem.get(origem, 0) + 1
            
    for origem in num_total_origem:
        ganhos = num_ganhos_origem.get(origem, 0)
        total = num_total_origem[origem]
        tax[origem] = ganhos / total
    
    print(f"Taxa de conversão:")
    for origem in tax:
        taxa = tax[origem]
        print(f"{origem}: {taxa:.2%}")
         
     
    
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
    
