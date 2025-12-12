class Livro:
   
    def __init__(self, id : int, titulo : str, autor : str, ano : int):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
 
 
#Funcoes uteis

def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = valor
        
def busca_binaria(lista: list[int], valor):
    ini, fim = 0, len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1     

def busca_sequencial(lista: list[int], valor: int) -> int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  
    return -1  



  
        
#a) Função para verificar id

def idlivro_lista(lista, id_busca):
    
    ids = []
    for livro in lista:
        ids.append(livro.id)
    
    insercao(ids)       
    esta_na_lista = busca_binaria(ids, id_busca)
    
    if esta_na_lista == -1:
        return False
    else:
        return True
    
#b) função anos dos livros

def intervalos_anos(lista, ano_min, ano_max):
    
    livros_validos = []
    anos = []
    for livro in lista:
        anos.append(livro.ano)
        
    for ano in range(ano_min, ano_max + 1):
        ano_atual = busca_sequencial(anos, ano) 
        if ano_atual != -1:
            livros_validos.append(lista[ano_atual])
            
    return livros_validos



def main():
    lista = []
    qnt = int(input("Quantidade de livros: "))

    for i in range(qnt): 
        id = int(input("Id do livro: "))
        titulo = input("Titulo do livro: ")
        autor = input("Autor do livro: ")
        ano = int(input("Ano do livro: "))
        lista.append(Livro(id, titulo, autor, ano))
        print('-' * 30)
        
    id_busca = int(input("Digite um id para busca: "))
    esta_na_lista = (idlivro_lista(lista, id_busca))
    if esta_na_lista == True:
        print("O id do livro está na lista")
    elif esta_na_lista == False:
        print("O id do livro não está na lista")
    print('-' * 40)
        
    ano_min = int(input("Digite um ano minimo de busca: "))
    ano_max = int(input("Digite um ano maximo de busca: "))
    print("LIVROS VALIDOS")
    lista_validos = (intervalos_anos(lista, ano_min, ano_max))
    
    
    print(f"{'Id':<10}{'Titulo':<20}{'Autor':<20}{'Ano':<10}")
    print('-' * 40)
    
    for livros in lista_validos:
        print(f'{livros.id :<10}{livros.titulo :<20}{livros.autor :<20}{livros.ano :<10}')
    
        
        
 
       
#Programa principal
if __name__ == '__main__':
    main()
    
    
#Bom natal e feliz ano novo professor!
    