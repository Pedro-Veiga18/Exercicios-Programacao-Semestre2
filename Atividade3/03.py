class Professor:
    def __init__(self, nome : str, num_aulas_semanais : int, hora_aula : float, titulo : str):
        self.nome = nome
        self.num_aulas_semanais = num_aulas_semanais
        self.hora_aula = hora_aula
        self.titulo = titulo
      


#Salário Base
def salario_base_calculo(lista):
    
    salarios_base = []
    
    for professor in lista:
        sal_base = professor.num_aulas_semanais * 4.5 * professor.hora_aula
       
        if professor.titulo == 'mestre':
            sal_base += 0.085 * sal_base
            salarios_base.append(sal_base)
        
        elif professor.titulo == 'doutor':
            sal_base += 0.12 * sal_base
            salarios_base.append(sal_base)
            
        else:
            salarios_base.append(sal_base)
            
    return salarios_base

#Adicional de hora-atividade
def add_hora_atividade_calculo(salarios_base):
    
    add_hora_salarios_base = []
    
    for i in range(len(salarios_base)):
        salarios_base[i] += 0.05 * salarios_base[i]
        add_hora_salarios_base.append(salarios_base[i])
        
    return add_hora_salarios_base

#Descanso Semanal Remunerado
def descanso_remunerado_calculo(add_hora_salarios_base):
    
    salarios_bruto = []
    
    for j in range(len(add_hora_salarios_base)):
        add_hora_salarios_base[j] += (add_hora_salarios_base[j] / 6)
        salarios_bruto.append(add_hora_salarios_base[j])
        
    return salarios_bruto
        
    
            

def main():
    lista = []

    for i in range(3): 
        nome = input("Nome do professor: ")
        num_aulas_semanais = int(input("Número de aulas semanais: "))
        hora_aula = float(input("Valor da hora-aula: "))   
        titulo = input("Titulo do professor: ")
        lista.append(Professor(nome, num_aulas_semanais, hora_aula, titulo))
        print('-' * 30)
        
    salarios_base = salario_base_calculo(lista)
    add_hora_salarios_base = add_hora_atividade_calculo(salarios_base)
    salarios_bruto = descanso_remunerado_calculo(add_hora_salarios_base)
        
      
    
    
    print(f"{'Nome':<15}{'Titulo do professor':<25}{'Salário Bruto':<15}")
    print('-' * 55)
    
    for k in range(len(salarios_bruto)):
        print(f'{lista[k].nome :<15}{lista[k].titulo :<25}{salarios_bruto[k] :<15.2f}')
    
        
        
 
       
#Programa principal
if __name__ == '__main__':
    main()