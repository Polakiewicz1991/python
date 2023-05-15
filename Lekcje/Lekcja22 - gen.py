def gen():
    i = 0
    while i < 5:
        yield i #to co return bez zwracania return/ generator
        i+= 1

for i in gen():
    print(i)

print(tuple(gen()))

def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1

for i in parzyste(16):
    print(i)

print(tuple(parzyste(50)))