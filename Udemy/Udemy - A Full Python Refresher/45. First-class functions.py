def divide(divided, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Kurdebele Divisor cannot be 0")

    return divided / divisor

def calculate(*values, operator):
    return operator(*values)

resultat = calculate(20,5, operator=divide)

print(resultat)

def serch(sequence, excepted, finder):
    for elem in sequence:
        if finder(elem) == excepted:
            return elem
    raise RuntimeError(f"Could not find an elemenet with {excepted}")

friends = [{"name": "Bob", "age": 25},
            {"name": "xD", "age": 4},
            {"name": "gumwo", "age": 24}]

def getFriendName(friend):
    return friend["name"]

from operator import itemgetter
print(serch(friends, "xD",getFriendName))
print(serch(friends, "xD",lambda friend: friend["name"]))
print(serch(friends, "xD",itemgetter("name")))