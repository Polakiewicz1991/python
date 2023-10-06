from functools import reduce
sum = lambda a,b: a + b

print(sum(4,5))
print(sum(14,5))

def generateLambda(num):
    return lambda a: a*num

doubler = generateLambda(2)

print(doubler(4))

listData = [0,1,2,3]

resultList = list(map(lambda a:a*3,listData))
print(resultList)


resultResultList = list(filter(lambda a:a>5,resultList))
print(resultResultList)

joinText = reduce( lambda x,y: x + ' ' + y,['Paweł',"Kuba"])
print(joinText)