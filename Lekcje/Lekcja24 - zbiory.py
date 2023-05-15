# set / zbiór
liczby1 = {0, 1, 2, 4}

#zmiana listy na zbiór
slowa = set(['a','b','c'])


print(liczby1)
print(slowa)

#dodanie liczby 5 do zbioru
liczby1.add(5)

print(liczby1)

liczby1.remove(0)
print(liczby1)

#dodanie liczby 5 nie zmieni zbioru jeżeli 5 zawiera się już w zbiorze

liczby1.add(5)
print(liczby1)

#sprawdzanie czy wartość znajduje się w zbiorze
print(1 in liczby1)
print('a' in liczby1)

# nie będzie działało bo 0 się powtarza
# loczby2 = {0, 0, 1,3 }
# print(liczby2)

liczby2 = {3,4,5,6}
#wyświetl liczby zawierające się w zbiorze liczny1 lub liczby2
print(liczby1 | liczby2)
#wyświetl liczby zawierające się w zbiorze liczny1 i liczby2
print(liczby1 & liczby2)
#wyświetl liczby zawierające liczny1 - liczby2
print(liczby1 - liczby2)
#wyświetl liczby zawierające liczny2 - liczby1
print(liczby2 - liczby1)
#wyświetl liczby zawierające liczny1 ^ liczby2 - exor
print(liczby1 ^ liczby2)
