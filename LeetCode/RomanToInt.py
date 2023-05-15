
def roman_to_int(iroman: str) -> int:
    y = 0
    C = 0
    X = 0
    I = 0
    for i in iroman:
        if i == 'M':
            if C == 1:
                y += 900
                C = 0
            elif C > 1:
                print("Błąd kalkulacji")
                return -1
            else:
                y += 1000
        elif i == 'D':
            if C == 1:
                y += 400
                C = 0
            elif C > 1:
                print("Błąd kalkulacji")
                return -1
            else:
                y += 500
        elif i == 'L':
            if X == 1:
                y += 40
                X = 0
            elif X > 1:
                print("Błąd kalkulacji")
                return -1
            else:
                y += 50
        elif i == 'V':
            if I == 1:
                y += 4
                I = 0
            else:
                y += 5
        elif i == 'C':
            C += 1
        elif i == 'X':
            X += 1
        elif i == 'I':
             I += 1
    if I > 0 and I <= 3:
        y += I + (X * 10) + (C * 100)
        I = 0
    else:
        print("Błąd kalkulacji")
        return -1

    return y


def RomanToInt2(Roman: str) -> int:
    lista = ('M', 'D', 'C', 'L', 'X', 'V', 'I')

    sum = 0
    i = 0
    j = 1000
    while j >= 2:
        digits = 0
        tens = 0
        hundreds = 0
        slownik = {'M' : 1000,'D' : 500,'C' : 100,'L' : 50,'X' : 10,'V' : 5,'I' : 1}
        print(lista[i : i+3])

        for x in (Roman):

            if x == lista[i + 2]:
                if digits >=0:
                    digits += 1
            elif x == lista[i+1]:
                tens += 1
                if digits == 1:
                    digits = -1
                elif hundreds == 1:
                    hundreds = 0
            elif x == lista[i]:
                hundreds += 1
                if digits == 1:
                    digits = -1

        sum += (j / 10 * digits) + (j / 2 * tens) + (j * 1 * hundreds)
        print("100: ",hundreds," 10: ",tens," 1: ",digits)
        print(sum)
        i += 2
        j = j / 10

    return sum



print(roman_to_int("MCMLXIX"))
print(RomanToInt2("MCMLXIX"))