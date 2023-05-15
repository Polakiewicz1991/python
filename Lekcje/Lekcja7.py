#lista = [0,1,3,4...]
lista = [1,2, "xD", ":D", "-.-"]
lista = [1,2, "xD", ":D", "-.-", ]
print(lista)
print(lista[0])
print(lista[4])

lista[2] =  3
print(lista)

tekst = "Hello world"
print(tekst[1])

print(lista + ["g", "f"])
print(lista * 3)
print("Ilość elementów: ", len(lista))

lista.append("e")
print(lista)

lista.append(["h", "j"])
print(lista)
print(lista[6][0]) #lista w liście
print(lista[6]) #lista w liście

lista.insert(3,3)
print(lista)

print("Ilość znaków 3:",lista.count(3))
print("Index znaku 1 :",lista.index(1))


lista.remove('e')
print(lista)

lista2 = [1,20,35,-5,9]
print(lista2)
print("Minimum:",min(lista2))
print("Maksimum:",max(lista2))
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)
lista2.clear()
print(lista2)
print(len(lista2))