def teste(a, b, c):
    if a > b and b > c:
        resp = a + b
    elif a < b and b < a:
        resp = a - b
    else:
        resp = a + b + c
    return resp


print(teste(-1, 4, -1))