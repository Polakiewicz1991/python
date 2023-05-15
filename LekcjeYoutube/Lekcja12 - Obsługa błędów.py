#obsługa wyjądków
x = 12
y = 0

try:
    lista = [1,2]
    print(lista[0])
    print(x + "!")
    print("Linijka po operacj")
# except ZeroDivisionError:
#     print("Nic się nie stało")
# except TypeError:
#     print("Błąd typu danych")
except (TypeError,ZeroDivisionError):
    print("Błąd")
except:
    print("Przejęcie innych wyjądków")
finally: #pojawia sie na końcu, wykona się za każdym razem po try i except, z błędem czy bez


print("dalsze instr...")

try:
    print(x / y)
    print("Linijka po operacj")
except ZeroDivisionError:
    print("Nic się nie stało")

print("dalsze instr...")