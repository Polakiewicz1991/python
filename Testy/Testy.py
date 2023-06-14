# List of strings
l = ['sat', 'bat', 'cat', 'mat']


for x in zip(*l):
    print(x)

z = list(zip(*l))
y = tuple(zip(*l))
x = set(zip(*l))
print("z", z)
print("y", y)
print("x", x)


test = list(map(list, l))
print(test)

# String from list
testStr = ''
for x in test:
    testStr += ''.join(x) + ' '
print(testStr)