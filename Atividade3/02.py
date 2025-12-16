class Rota:
    def __init__(self, nome : str, trecho : list[dict], delay_sinal : float = 45.0):
        self.nome = nome
        self.trecho = trecho
        self.delay_sinal = delay_sinal
        
        
    #a)
    def tempo_total_min(self) -> float:
        tempo_h = 0
        soma_semaforos = 0

        for trecho in self.trecho:
            tempo_h += trecho['dist_km'] / trecho['vel_kmh']
            soma_semaforos += trecho['semaforos']

        paradas_min = soma_semaforos * (self.delay_sinal / 60)
        tempo_total_min = 60 * tempo_h + paradas_min
        return tempo_total_min
    
    #b)
    def velocidade_media_kmh(self) -> float:
        distancia_total = 0
        
        for trecho in self.trecho:
            distancia_total += trecho['dist_km']
        
        horas = self.tempo_total_min() / 60 
        velocidade_media = distancia_total / horas
        
        return velocidade_media
    
    #atende janela
    def atende_janela(self, inicio_min : float, fim_min : float) -> bool:
        tempo = self.tempo_total_min()
        
        if tempo >= inicio_min and tempo <= fim_min:
            return True
        else:
            return False
        
    #c)
    def custo_emissao(self, kg_co2_km : float) -> float:
        distancia_total = 0
        
        for trecho in self.trecho:
            distancia_total += trecho['dist_km']
            
        emissao = distancia_total * kg_co2_km
        
        return emissao, distancia_total
    
#Funções uteis
def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = valor
               


#Função principal 
def main():
    lista_rotas = []    
    qnt_rotas = int(input("Quantidade de rotas: "))

    for i in range(qnt_rotas): 
        nome = input("Nome da rota: ")
        
        trechos = []
        qnt_trechos = int(input("Quantidade de trechos na rota: "))
        
        for j in range(qnt_trechos):
            dist_km = float(input("Distância em km: "))
            vel_kmh = float(input("Velocidade em km/h: "))
            semaforos = int(input("Quantidade de semáforos: "))        
            trechos.append({'dist_km': dist_km, 'vel_kmh' : vel_kmh, 'semaforos' : semaforos})       
          
        delay_sinal = float(input("Tempo, em segundos, do atraso médio por semáforo: "))   
        
        lista_rotas.append(Rota(nome, trechos, delay_sinal,))
        print('-' * 30)
        
    
    #d)
    lista_tempos_totais = []
    for rota in lista_rotas:
        tempo = rota.tempo_total_min()
        lista_tempos_totais.append(tempo)
        
    insercao(lista_tempos_totais)
    
    print("Ranking por Tempo Total")
    print()
    print(f"{'Ranking':<15}{'Rota':<15}{'Tempo(min)':<15}{'Vel.media(km/h)':<15}")
    print('-' * 60)
    
    ranking = 1
    for tempo in lista_tempos_totais:
        for rota in lista_rotas:
            if tempo == rota.tempo_total_min():
                print(f"{ranking:<15}{rota.nome:<15}{tempo:<15.2f}{rota.velocidade_media_kmh():<15.2f}")
                ranking +=1
                break
            
    #e)
    print('-' * 60)
    inicio_min = float(input("Digite um tempo minimo, em minutos, para a Rota: "))
    fim_min = float(input("Digite um tempo máximo, em minutos, para a Rota: "))
    print()
    
    print(f"Rotas que atendem a janela de {inicio_min}-{fim_min} minutos")
    
    for rota in lista_rotas:
        if rota.atende_janela(inicio_min, fim_min) == True:
            print(f"- {rota.nome} (Tempo: {rota.tempo_total_min():.2f} min)")
            
    #f)
    print('-' * 60)
    kg_co2_km = 0.192
    print("Comparativo de Emissões")
    for rota in lista_rotas:
        emissao, distancia_total = rota.custo_emissao(kg_co2_km)
        print(f"{rota.nome} | Dist: {distancia_total:.2f}km | Emissão: {emissao:.2f}kg CO2")    
 
       
#Programa principal
if __name__ == '__main__':
    main()      
        
     