#immutable: int, float, bool, str, frozenset

def modifyString(inputString):
    print(id(inputString))
    inputString += '!'
    print(id(inputString))
    print(inputString, '\n')

helloString = "Hello wordl"
print(id(helloString))
modifyString(helloString)
print(id(helloString))
print(helloString, '\n')

#mutable: set, dict, list

def modifyList(list):
    print(id(list))
    list.append(10)
    list.append(3)
    print(id(list))

print("\n\n\n")
testList = [0,1,2]
print(id(testList))
modifyList(testList)
print(id(testList))