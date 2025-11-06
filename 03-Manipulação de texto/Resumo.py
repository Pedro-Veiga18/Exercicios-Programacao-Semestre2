s = "Pedro Veiga"
print(s)

#Espaço em branco entra na contagem do tamanho
print(len(s))

#Concatenação
w = "Marcela Andretto"
print(s + w)
print("Pedro Veiga", "Marcela Andretto")

#Substituição
print(s.replace("Veiga", "Andretto"))

#Começa e Termina
print(s.startswith("Pedro"))
print(w.startswith("Pedro"))
print(s.endswith("Veiga"))
print(w.endswith("Veiga"))

#Contagem
amo = "amo amo amo amoamo"
print(amo.count("amo"))

#Maisculo
a = "arroz feijao"
print(a.capitalize())

#Verificacao de números e letras
print("123".isdigit())
print("123a".isdigit())
print("123a".isalnum())

#Caracteres individuais
for i in range(len(s)):
    print(s[i])

#Slices
print(s[:5])
print(s[6:])

print(s[::2]) #índices pares
print(s[1::2]) #índicies ímpares

print(s[::-1])

#Formatação antiga
frase = "Eu tenho {0} cachorro, {1} peixes e {2} avós".format(1, 5, 3)
print(frase)

#Formatação nova
quant_c = 1
quant_p = 5
quant_a = 3
print(f"Eu tenho {quant_c} cachorro, {quant_p} peixes e {quant_a} avós")

#Exemplos
print(f"Qual o seu nome ? {s.upper() + '!' * 5}")

sunny = "Sunny"
boy = "Boy"
print(f"{sunny}\n" f"{boy}")