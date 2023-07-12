class Solution:
    def intToRoman(self, num: int) -> str:
        romeInt = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        intRome = {10000: 'D2',5000: 'D1',1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

        strResult = ""

        digits = [0] * 4
        #3 => "III"  3//5,3%5 => 0,3
        #7 => "VII"  7//5,7%5 => 1,2
        #9 => "IX"   9//5,9#5 => 1,4
        i = len(digits) - 1

        while i >= 0:
            j = 10 ** (i+1)
            digits[i] =  int((num % j) //(j / 10)) #- sum(digits)
            print(f"digits[{i}]",digits[i]," j:", j)

            x,y = digits[i]//(5), digits[i]%(5)

            print("x:", x, " y:", y)
            if y == 4:
                if x == 0:
                    strResult += intRome[(j / 10)] + intRome[j/2]
                else:
                    strResult += intRome[(j / 10)] + intRome[j]
            else:
                strResult += intRome[(j/2)] * x + intRome[(j/10)] * y

            print(strResult)
            i -= 1
            # print(i)
        # digits.reverse()
        # print("digits", digits)

        # digits[0] = num % 10
        # digits[1] = num % 100 - digits[0]
        # digits[2] = num % 1000 - digits[1] - digits[0]
        # digits[3] = num %10000 - digits[2] - digits[1] - digits[0]




Wynik = Solution()

num = 3
Wynik1 = Wynik.intToRoman(num= num) #"III"

num = 58
Wynik2 = Wynik.intToRoman(num= num) #"LVIII"

num = 1994
Wynik2 = Wynik.intToRoman(num= num) #"MCMXCIV"
