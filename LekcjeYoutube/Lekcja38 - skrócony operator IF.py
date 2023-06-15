print("Prawdza") if 5 > 2 else print("Nieprawda")
txt = ("Prawdza") if 5 > 5 else ("Nieprawda")

print(txt)

for i in range(10):
    if i > 5:
        continue
else:
    print("Koniec")

for i in range(10):
    if i > 5:
        break
else:   #działa tylko jak instrukcia wykona się do końca
    print("Koniec")


try:
    a = 5/0
except ZeroDivisionError:
    print("błąd")
else: #Wykona sie jeżeli wykona się try
    print("koniec  try")
finally:
    print("Finally wykonuje się zawsze")
