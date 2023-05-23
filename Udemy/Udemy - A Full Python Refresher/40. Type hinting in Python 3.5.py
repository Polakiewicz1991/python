from typing import List

def list_avg(sequence: list) -> float:
    return  sum(sequence) / len(sequence)

print(list_avg([123]))

class Book:
    TYPES = ("hardcover","peperback")
    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<This is {self.name}, {self.book_type} and it weights {self.weight}g>"

    @classmethod
    def hardcover(self, name: str, weight_raw: int) -> "Book":
        return Book(name, Book.TYPES[0], weight_raw + 100)

    @classmethod #podobno lepiej stosować cls zamiast nazwy klasy
    def peperback(self, name: str, weight_raw: int) -> "Book": #zwrócenie klasy w cudzysłowie
        return cls(name, cls.TYPES[1], weight_raw + 0)

class BookShelf():
    def __init__(self,books: List[Book]):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"

book1 = Book.hardcover("xD",2)
book2 = Book.peperback(":D",3)
bookShelf = BookShelf([book1,book2])

print(bookShelf)
for book in bookShelf.books:
    print(book)