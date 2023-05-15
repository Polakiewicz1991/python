def roman_to_int(roman: str) -> int:
    y = 0
    C = 0
    X = 0
    I = 0
    for i in roman:

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
            if I == 1: I -= 2
            X += 1
        elif i == 'I':
             I += 1
    if I <= 3:
        y += I + (X * 10) + (C * 100)
        I = 0
    else:
        print("Błąd kalkulacji")
        return -1

    return y

def RomanToInt2(Roman: str) -> int:
    lista = ([None],[None],'M', 'D', 'C', 'L', 'X', 'V', 'I',[None])

    sum = 0
    i = 0
    j = 10000
    while j >= 2:
        digits = 0
        tens = 0
        hundreds = 0
        lock = False
        slownik = {'M' : 1000,'D' : 500,'C' : 100,'L' : 50,'X' : 10,'V' : 5,'I' : 1}
        print(lista[i : i+4])

        for x in (Roman):
            if lock == False:
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
                elif x == lista[i+3]:
                    lock = True

        sum += (j / 10 * digits) + (j / 2 * tens) + (j * 1 * hundreds)
        print("100: ",hundreds," 10: ",tens," 1: ",digits)
        print(sum)
        i += 2
        j = j / 10

    return sum

def RomanToIntInternet(Roman: str) -> int:
    Values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    # print(Roman)
    # print(len(Roman))
    # print(range(len(Roman)))
    #MCMLXXIX
    for i in range(len(Roman)):
        if (i + 1) < len(Roman) and Values[Roman[i+1]] > Values[Roman[i]]:
        #if Values[Roman[i+1]] > Values[Roman[i]] and (i + 1) < len(Roman):
            sum -= Values[Roman[i]]
        else:
            sum += Values[Roman[i]]
        # print(Values[Roman[i]])
        # print(sum)
    return sum
RomanValue: str = input("Podaj liczbę rzymską:" )
print(roman_to_int(RomanValue))
print(RomanToInt2(RomanValue))
print(RomanToIntInternet(RomanValue))