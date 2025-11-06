#Demonstar o código ASCII das letras de uma palavra

a = input("Informe uma palavra: ").lower()
for letra in a:
    print(f"letra = {letra} | código = {ord(letra)}")
    
#Imprimir os caracteres de uma lista de códigos ASCII
    
lista =[47, 69, 97, 124]
for i in lista:
    print(chr(i))