def func(x):
    return x * x

zmienna = func

print(zmienna(5))

def func2(f1, x):
    return f1(x) * x

print(func2(func,5))

#rekurencja = rekursja
def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

print(silnia(15))