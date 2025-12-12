class Hospede:
    
    def __init__(self, nome : str):
        self.nome = nome
        
class Quarto:
    
    def __init__(self, numero : int, vl_diaria : float):
        self.numero = numero
        self.vl_diaria = vl_diaria
        
class Reserva:
    
    def __init__(self, hospede : Hospede, quarto : Quarto, total_diarias : int):
        self.hospede = hospede
        self.quarto = quarto
        self.total_diarias = total_diarias



#b) função de impressao

def imprimir_reservas(lista_r):
    print(f"{'Hóspede':<20}{'Quarto':<10}{'Diária':<10}")
    print('-' * 40)
    
    for reservas in lista_r:
        print(f'{reservas.hospede.nome :<20}{reservas.quarto.numero :<10}{reservas.quarto.vl_diaria :<10.2f}')

#c) Funcao valor total pousada

def vl_total_pousada(lista_r):
    
    total = 0
    for reservas in lista_r:
        total += reservas.quarto.vl_diaria * reservas.total_diarias
    print(f"Valor total de reservas até o momento: {total: .2f}")
    

#d) Funcao valor da estadia do hospede

def vl_hospede_estadia(lista_r, hospede_nome):
    total_h = 0
    for reservas in lista_r:
        if reservas.hospede.nome == hospede_nome:
            total_h += reservas.quarto.vl_diaria * reservas.total_diarias
            
    print(f"O valor da estadia do hóspede {hospede_nome} é: {total_h}")
        

def main():
    
    #a) listas

    print("Considere o mesmo número para a quantidade de hóspedes, quartos e reservas.")
    #Lista hospede
    lista_h = []
    qnt_h = int(input("Quantidade de hóspedes: "))

    for i in range(qnt_h): 
        nome = input("Nome: ")
        lista_h.append(Hospede(nome))
        print('-' * 30)
 
    #Lista quarto   
    lista_q = []
    qnt_q = int(input("Quantidade de quartos: "))

    for j in range(qnt_q): 
        numero = int(input("Numero: "))
        vl_diaria = float(input("Valor da diária: "))
        lista_q.append(Quarto(numero, vl_diaria))
        print('-' * 30)

    #Lista reserva  
    lista_r = []
    qnt_r = int(input("Quantidade de reservas: "))

    for k in range(qnt_r):
        total_diarias = int(input("Total de diarias: "))
        lista_r.append(Reserva(lista_h[k], lista_q[k], total_diarias))
        
        
    imprimir_reservas(lista_r)
    vl_total_pousada(lista_r)
    
    hospede_nome = input("Insira o nome do hospede para calcular o valor de sua estadia: ")
    vl_hospede_estadia(lista_r, hospede_nome)
        


#Programa principal
if __name__ == '__main__':
    main()
    
    
#Bom natal e feliz ano novo professor!
    



  