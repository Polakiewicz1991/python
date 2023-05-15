def funkcja(arg1,arg2 = "world", *args, **kwargs):
    print(arg1,arg2,args,len(args),kwargs)

    for x in args:
        print(x)

    print(kwargs)
    print(kwargs.items())
    print(kwargs.items())
    for x in kwargs:
        print(x)
funkcja("Hello")
funkcja("Hi","youtube")

funkcja("Hi","youtube","!","xD", autor = "Paweł", rok=2023)

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

