import typing
class Line():
    def __init__(self,maxWidth):
        self.line = []
        self.lenght = - 1
        self.maxWidth = maxWidth

    def __str__(self):
        return f"{self.line} / {self.lenght}"

    def append(self,word: str):
        if self.lenght <= self.maxWidth:
            self.line.append(word)
            self.lenght += len(word) + 1
        else:
            print("Linia za długa")

    def split(self):
        for word in self.line:
            pass

class Tekst():
    def __init__(self,*lines):
        self.lines = lines

    def __add__(self, newLine: Line):
        self.lines += newLine

    def __str__(self):
        return f"Jest {len(self.lines)} lini w tekscie."

class Solution(object):
    def fullJustify(self, words, maxWidth):
        lines = []
        linesLenIndex = 0
        linesLen = [-1]
        line = []
        strLine = ""

        for index, word in enumerate(words):
            if linesLen[linesLenIndex] + len(word) + 1 < maxWidth:
                linesLen[linesLenIndex] += len(word) + 1
                line.append(word)
            else:
                allSpacesNum = maxWidth - linesLen[linesLenIndex]
                if len(line) > 1:
                    oneSpace = (allSpacesNum // (len(line) - 1)) + 1
                    secSpace = allSpacesNum % (len(line) - 1)
                else:
                    oneSpace = 1
                    secSpace = 0

                print("allSpacesNum", allSpacesNum, "oneSpace", oneSpace, "secSpace", secSpace)

                for i, w in enumerate(line):
                    if i < len(line) - 1:
                        if secSpace > 0:
                            strLine += w + (" " * oneSpace) + (" ")
                            secSpace -= 1
                        else:
                            strLine += w + (" " * oneSpace)
                    else:
                        strLine += w
                print("strLine", "\"" + strLine + "\"", "len strLine", len(strLine))
                lines.append(strLine)
                strLine = ""

                linesLenIndex += 1
                linesLen.append(-1)
                line = []

                linesLen[linesLenIndex] += len(word) + 1
                line.append(word)

            if index == len(words) - 1:
                for i, w in enumerate(line):
                    if i < len(line) - 1:
                        strLine += w +  (" ")
                    else:
                        strLine += w + (" ") * (maxWidth -len(strLine))
                print("strLine", "\"" + strLine + "\"", "len strLine", len(strLine))
                lines.append(strLine)


        print(linesLen)
        return lines

Wynik = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Wynik1 = Wynik.fullJustify(words= words,maxWidth= maxWidth)
print("Wynik1", Wynik1)

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Wynik1 = Wynik.fullJustify(words= words,maxWidth= maxWidth)
print("Wynik1", Wynik1)