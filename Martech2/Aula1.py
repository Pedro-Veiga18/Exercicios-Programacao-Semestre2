import random

def descobrir(n, grf_env):
    k = n.bit_length()
    testadores = [0] * k
    for i in range(k):
        if grf_env & (1 << i) != 0:
            testadores[i] = 1
            
            
    #converter
    resultado = 0
    for i in range(k):
        if testadores[i] == 1:
            resultado += 1 << i
            
    return resultado
    
    
    
    
#Programa principal
n = 8
grf_env = random.randint(0, n-1)
resultado = descobrir(n, grf_env)
print(f"garrafa envenenada {grf_env}")
print(f"garrafa envenenada descoberta {resultado}")