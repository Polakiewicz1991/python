def add_two_friends():
    friend = input("Dodaj kolege: ")
    friend2 = input("Dodaj jeszcze jednego kolege: ")
    friends_in_function = friends + [friend, friend2]  # zadziała tylko po zdefiniowaniu friends w programie
    print(friends_in_function)

friends = ["Kuba" , "Michu"]

def add_friend():
     friend = input("Dodaj kolege: ")
     # friends =  friends + friend #nie będzie działać bo zmienna zdefiniowana jest w funkcji i odnosi się do siebie samej
     friends_in_function = friends + [friend]
     print(friends_in_function)

add_friend()
add_two_friends()


default_y = 3

def addInt(x,y=default_y):
    return x + y

print(addInt(2))


default_y = 8 #zmiana default_y nie wpływa na wynik funkcji addInt,
            #ponieważ funkcja przyjmuje wartość zdefiniowaną przed nią samą

print(addInt(2))