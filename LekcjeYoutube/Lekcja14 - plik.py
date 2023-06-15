#Operowanie na plikach .txt
#domyślnie do odczytu bez parametru "w" plik = open("test.txt")
#tylko do odczytu z parametrem "r" plik = open("test.txt", "r")
#dodawanie do pliku za pomocą "a" append

plik = open("test.txt", "a")

#jeżeli jest w trybie do zapisu zwraca true writable()
print(plik.writable())

if plik.writable():
    ile = plik.write(input("Wprowadź tekst: ") + "\n")
    print("Zapisano: ", ile)
plik.close()

plik = open("test.txt", "r")

if plik.readable():
    tekst =  plik.read()
    print("Zawartość pliku (read): ",tekst),

    plik.seek(0)
    #lista wszystkich linii
    tekst = plik.readlines()
    print(tekst)
    print("Zawartość pliku (readline): ", tekst),
    for l in tekst:
        print("for l in tekst: print l)", l)

    for l in plik:
        print("for l in plik: print l)",l)

plik.close()

