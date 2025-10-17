def func(a, b, c):
    x = (a and b) and ((c or a or b) or (not(a) and c))
    return x

print(func(False, True, False))