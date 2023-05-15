def decorator(func):
    def wrapper():
        print("-------")
        func()
        print("-------")
    return wrapper


def hello():
    print("Hello world")

hello = decorator(hello)

hello()

@decorator
def witaj():
    print("Witaj świecie")

witaj()