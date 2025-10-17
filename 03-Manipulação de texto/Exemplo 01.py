a = input("Informe uma palavra: ").lower()
for letra in a:
    print(f"letra = {letra} | código = {ord(letra)}")
    
lista =[47, 69, 97, 124]
for i in lista:
    print(chr(i))