#krotka krotku
#tuple

#index = (0,1,2, 3, 4, 5, 6)
krotka = (2,4,8,16,32,64,128)
print(krotka[0])
print(krotka)

#nie wspiera modyfikacji elementów krotki
# krotka[0] = 1

print("Ilość elementów krotki:", krotka.count(2))
print("Indeks elementu krotki:", krotka.index(64))

print("\nWycinki:")
print(krotka[0:3]) # 0,1,2 bez 3
print(krotka[3:5]) # 3,4 bez 5
print(krotka[3:55])
print(krotka[-3:-1]) # 6-3 do 6-1
print(krotka[0:7:2]) #początek:koniec:skok
print(krotka[0:]) #caość
print(krotka[0::2]) #początek:koniec:skok
print(krotka[:3])
print(krotka[::-1]) #odwrócenie krotki