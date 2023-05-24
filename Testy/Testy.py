# List of strings
l = ['sat', 'bat', 'cat', 'mat']

test = list(map(list, l))
print(test)

# String from list
testStr = ''
for x in test:
    testStr += ''.join(x) + ' '
print(testStr)