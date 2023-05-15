#formatowanie stringów

lista = list(range(10))

print(lista)

#tworzenie nowej listy z elementami 2x większymi mnożenie wszystkich elementów z listy
nowa = [i * 2 for i in lista]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#nowa2 = [i + 2 for i in lista if i % 2 == 0]
nowa2 = [i + 2 for i in lista if i < 4]
print("Nowa lista:", nowa)
#Nowa lista: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print("Nowa2 lista:", nowa2)
#Nowa2 lista: [2, 3, 4, 5]

#formatowanie stringów
argumenty = ["Sebastian" , 24]
teks = "Cześć mam naimię {0} i mam {1} lata".format(argumenty[0],argumenty[1])
print(teks)
teks = "Cześć mam naimię {imie} i mam {wiek} lata, {imie}".format(imie = argumenty[0],wiek = argumenty[1])
print(teks)
