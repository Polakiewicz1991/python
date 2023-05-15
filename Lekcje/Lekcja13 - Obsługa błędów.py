#przechwytywanie wyjądków

def dielenie(x,y):
    assert y != 0, "Y != 0"
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez 0 xDD") #w innych throw
    print(x / y)

try:
    dielenie(2,2)
except ZeroDivisionError:
    print("Somfing is not jes")
    raise

dielenie(2,0)