""" 
Implemente uma função em Python que recebe uma lista de tuplas, onde cada
tupla representa um intervalo numérico [a, b], com a ≤ b. A função deve
realizar as seguintes operações:
a) unir intervalos que se sobrepõem: se dois intervalos [a, b] e [c, d] se
sobrepõem (ou seja, b ≥ c), eles devem ser unidos em um único intervalo.
b) contar o número total de intervalos resultantes.
c) Retornar a soma total do comprimento de todos os intervalos resultantes.
"""

lista = [(2, 4), (1, 3), (3, 5), (7, 10)]

lista.sort()

print(lista)

