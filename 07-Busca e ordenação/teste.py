import util
from random import randint
lista = [randint(1,500) for _ in range(10)]

print(util.bubblesort(lista))