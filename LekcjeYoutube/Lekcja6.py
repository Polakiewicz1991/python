from random import randint

# for i in  range(100):
#     print(randint(1,10))

los = randint(1,10)
odp = -1

i = 0
print("Zgadnij liczę z przedziału od 1 do 10")
while odp != los:
    i += 1
    odp = int(input("Podaj wartość:"))
    if odp == los:
        print("Wylosowana watość to: ", odp)
        print("Odgadłeś za: ", i, "razem")
        break