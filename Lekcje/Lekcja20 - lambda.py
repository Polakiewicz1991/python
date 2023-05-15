#lambda

def funkcja(f, liczba):
    return f(liczba)

print(funkcja(lambda x: x * x,3))

def kwadrat(x):
    return  x * x
print(kwadrat(5))

wyn = (lambda x: x * x)(9) #wywołanie funkcji lambda
print(wyn)

wyn2 = (lambda x: x * x) #wywołanie funkcji lambda bez argumentu
print(wyn2(2))

wyn3 = (lambda x,y: x * y) #wywołanie funkcji lambda z kilkoma argumentami
print(wyn3(2,6))


