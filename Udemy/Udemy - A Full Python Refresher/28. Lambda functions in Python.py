add = lambda x, y: x + y

print(add(5,7))

print((lambda x, y: x + y)(5,7))

def double(x):
    return x * 2

sequence = [1,2,3,4,5]
doubled =[ double(x) for x in sequence]
print(doubled)
doubled = map(double, sequence) #zwróci map object
doubled = list(map(double, sequence))
print(doubled)
doubled =[ (lambda x: x*2)(x) for x in sequence]
print(doubled)