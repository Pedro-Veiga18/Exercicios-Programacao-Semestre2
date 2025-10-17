
#Função criptografar
def criptografar(texto: str, deslocamento: int) -> str:
    aux = ""
    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra)
            aux += chr(((codigo - 97 + deslocamento) % 26) + 97)
        else:
            aux += letra
    return aux

#Função descriptografar
def descriptografar(texto_cripto: str, deslocamento: int) -> str:
    return criptografar(texto_cripto, -deslocamento)


#Função principal
def main():
    texto = input("Informe uma frase: ").lower()
    deslocamento = int(input("Deslocamento: "))
    texto_cripto = criptografar(texto, deslocamento)
    print(texto_cripto)
    texto_descripto = descriptografar(texto_cripto, deslocamento)
    print(texto_descripto)
    



#Programa principal
if __name__ == "__main__":
    main()