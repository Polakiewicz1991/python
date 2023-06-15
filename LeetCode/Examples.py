import itertools
def triowise(iterable):
    b, c = itertools.tee(iterable[1:])
    next(c, None)
    return zip(iterable, b, c)


for n, (a, b, c) in enumerate(triowise('ABCDEFGH')):
    n += 1 #inkrementacja w princie
    print('index', n, 'previous', a, 'current', b, 'next', c)

print("----------\n----------\n")

for n, (a, b, c) in enumerate(triowise('ABCDEFGH')):
    print('index', n, 'previous', a, 'current', b, 'next', c)


x =itertools.tee("ABC")
print(x)