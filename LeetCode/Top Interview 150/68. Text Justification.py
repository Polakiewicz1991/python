import typing
class Line():
    def __init__(self,maxWidth):
        self.line = []
        self.lenght = - 1
        self.maxWidth = maxWidth

    def __str__(self):
        return f"{self.line} / {self.lenght}"

    def append(self,word: str):
        self.line.append(word)
        self.lenght += len(word) + 1

    def split(self):
        for word in self.line:
class Solution(object):
    def fullJustify(self, words, maxWidth):
        lines = list[Line]
        linesLenIndex = 0
        linesLen = [0]
        line = []

        for index, word in enumerate(words):
            linesLen[linesLenIndex] += len(word) + 1
            if linesLen[linesLenIndex] < maxWidth + 1:
                line.append(word)
            else:
                lines.append(line)
                linesLen[linesLenIndex] -= len(word) + 1

                linesLenIndex += 1

                linesLen.append(0)
                line = []
                line.append(word)

            if index == len(words) - 1:
                lines.append(line)


        print(linesLen)
        # for x in lines:
        #     print(x.find(" "))
        return lines

Wynik = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Wynik1 = Wynik.fullJustify(words= words,maxWidth= maxWidth)
print("Wynik1", Wynik1)

