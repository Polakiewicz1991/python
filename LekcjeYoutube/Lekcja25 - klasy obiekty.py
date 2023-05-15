#klast i obiekty
#klasa z dużej
#funkcja z małej
#obiekt trzeba tworzyć z parametrami zdefiniowanymi w inicie
class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        self.zdrowy = True


    #print("Zdrowy w class: ",zdrowy)

    #jeżeli zmienna nie występuje w inicie nie musi być zdefioniowana przy tworzeniu obiektu
    #imie = "Pawel"

    #pierwszy argument mozna zmienic dowolnie
    #nie musi być self
    # def przedstawSie(kupa):
    #     kupa.imie
    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + ", mam na imie " +  self.imie + " lat " + str(self.wiek) + "."
    def stanZdrowia(self):
        if self.zdrowy == True:
            zdrowyStr = "zdrowy"
        else:
            zdrowyStr = "chory"

        return self.imie + " jest {zdrowie}.".format(zdrowie = zdrowyStr)


obiekt = Czlowiek("Paweł",32)
print(obiekt.przedstawSie("Witam"))
print(obiekt.imie)
print(obiekt.stanZdrowia())

print("\n----\n")

obiekt.zdrowy = False
print(obiekt.zdrowy)

print(obiekt.stanZdrowia())

obiekt2 = Czlowiek("Michał",22)
print(obiekt2.przedstawSie())
print(obiekt2.imie)
obiekt2.imie = "Kuba"

print(obiekt2.przedstawSie())
print(obiekt2.stanZdrowia())
print(obiekt2.imie)
print()