def named(**kwargs):
    print(kwargs)

named(name = "Bob", age = 25) # returns {'name': 'Bob', 'age': 25}

details = {"name" : "Bob", "age" : 25}
details2 = [{"name": "Bob", "age": 25},
            {"name": "xD", "age": 4},
            {"name": "gumwo", "age": 24}]
def named2(name,age):
    print(name,age)

named2(**details)
named2(**details2[1])

print("\nprint nicely")
def print_nicely(**kwargs):
    named(**kwargs)
    for imie, rok in kwargs.items():
        print(f"{imie}: {rok}")

print_nicely(name= "Bobas",age=1991)

print("\n both")
def both(*args,**kwargs):
    print(args)
    print(kwargs)

both(1,2,3,5,7,dupa="Kupa",kupa="z DUpa")