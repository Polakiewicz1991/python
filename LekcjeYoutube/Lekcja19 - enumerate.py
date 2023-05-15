plik = open("test.txt","r")
tekst = plik.read()
plik.close()


def policz(txt,znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik += 1
    return licznik

#print(policz(tekst,"a") +policz(tekst,"A"))
print(policz(tekst.lower(),"a"))

# for z in "ABCDEFGHIJKLMNOUPRSTUWXYZ0123456789":
#     z1 = enumerate(z)
#     ile = policz(tekst.upper(), z)
#     procent = 100 *  ile / len(tekst)
#     print("Litera{0} - {1}szt. - {2}%".format(z,ile,round(procent,2)))

print("\n")

for z in enumerate("ABCDEFGHIJKLMNOUPRSTUWXYZ0123456789"):
    ile = policz(tekst.upper(), z[1])
    procent = 100 *  ile / len(tekst)
    print("Litera{0} - {1}szt. - {2}%".format(z[1],ile,round(procent,2)))