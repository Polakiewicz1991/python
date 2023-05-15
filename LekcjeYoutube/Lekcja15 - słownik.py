#dictionary = słownik
#klucz i wartość
#key and value
slownik = {1: "Poniedziałek", 2:"Wtorek", 7:"Niedziela"}

print(slownik[7])

slownik[3] = "Środa"
slownik[4] = False
slownik["a"] = 1
print("\n")
for l in slownik:
    print(l)
    print(slownik[l])

print("\n")
for l in slownik.values():
    print(l)

print("\n")
#print(slownik[8])

print(slownik.get(8,"Inny dzien"))

slownik.pop(1)
print("\n")
for l in slownik.values():
    print(l)

print(slownik.items())
