#mapy i filtry

liczby = [2, 10, 12, 15, 20, 25, 30 , 35]

def funkcja(x):
    return x * 2

#Mapy
wynik = map(funkcja, liczby)
print(list(wynik))
#[4, 20, 24, 30, 40, 50, 60, 70] - * 2
print(list(map((lambda x: x + 2),liczby)))
#[4, 12, 14, 17, 22, 27, 32, 37] - +2
#filtry

wynik2 = filter(lambda x: x % 2 == 0,liczby)
print(list(wynik2))
#[2, 10, 12, 20, 30] - odfuiltrowanie parzystych