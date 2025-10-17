num_calls = 0


#Função de fibonacci
def fib(a):
    global num_calls
    if a == 0:
        return 0
    elif a == 1:
        return 1
    num_calls += 2
    return fib(a-1) + fib(a-2)
    
    
#Programa principal
n = int(input())
for i in range(n):
    a = int(input())
    num_calls = 0
    f = fib(a)
    print(f"fib({a}) = {num_calls} calls = {f}")
    