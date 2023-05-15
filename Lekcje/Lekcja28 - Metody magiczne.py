import math

class Punkt2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.odległość = math.sqrt(x**2 + y**2)
    def __add__(self, drugi):
        return Punkt2D(self.x + drugi.x, self.y + drugi.y)
    # def __add__(self, drugi, trzeci):
    #     return Punkt2D(self.x + drugi.x + trzeci.x, self.y + drugi.y + trzeci.y)
    def __lt__(self, drugi):
        return self.odległość < drugi.odległość

    def __eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y

    def __len__(self):
        return int(round(self.odległość,0))

p1 = Punkt2D(2, 5)
p4 = Punkt2D(2, 5)
p2 = Punkt2D(4, 5)
p3 = p1 + p2
print(p1 < p2)
print(p1.odległość)
print(p2.odległość)
print(p1 == p4)

print(len(p3))
print(p3.odległość)
print("x: ",p3.x,",y: ", p3.y)