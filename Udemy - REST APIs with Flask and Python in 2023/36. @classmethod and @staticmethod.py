class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method")

test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method()
ClassTest.static_method()

class Book:
    TYPES = ("hardcover","peperback")
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<This is {self.name}, {self.book_type} and it weights {self.weight}g>"

    @classmethod
    def hardcover(cls,name,weight_raw):
        return Book(name, Book.TYPES[0], weight_raw + 100)

    @classmethod #podobno lepiej stosować cls zamiast nazwy klasy
    def peperback(cls, name, weight_raw):
        return cls(name, cls.TYPES[1], weight_raw + 0)

print(Book.TYPES)

book1 = Book("Harry Potter", "komiks", 1500)
print(book1)
book2 = Book.hardcover("Wladca much",1600)
print(book2)
book3 = Book.peperback("Wladca much",1600)
print(book3)

