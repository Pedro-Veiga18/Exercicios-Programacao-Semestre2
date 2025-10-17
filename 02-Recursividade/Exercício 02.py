def somar(n:int) -> int:
    if n == 0: return 0
    return n % 10 + somar(n // 10)

print(somar(502708))