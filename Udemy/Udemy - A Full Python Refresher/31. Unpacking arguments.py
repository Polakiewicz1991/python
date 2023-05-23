def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(1,5,6))

def add(x, y):
    return x - y

nums = [3,4]
print(add(*nums)) #rozmiar listy i kolejność musi zgadzać się z ilością parametrów funkcji
nums = [4,3]
print(add(*nums)) #rozmiar listy i kolejność musi zgadzać się z ilością parametrów funkcji

numsDict = {"x": 18,"y": 9}
print(add(**numsDict)) #nazwy argumentów dziennika muszą zagadzać się z nazwami argumentów funkcji

def apply(*args, operator):
    print(args)
    if operator== "*":
        return multiply(*args)
        # return multiply(args) bez gwiazdki funkcja przujmie krotkę jako wartość i pomnoży ją przez jeden
    elif operator == "+":
        return sum(args)
    else:
        print("nie da rady")

print(apply(1,10,9,operator = "+"))
print(apply(5,8,9,operator = "*"))