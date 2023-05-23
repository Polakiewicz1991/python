from typing import List

class TooManyPagesReadError(ValueError):
    pass

class Book:
    TYPES = ("hardcover","peperback")
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return f"<This is {self.name}, read {self.pages_read} out of {self.page_count} pages>"

    def read(self,pages: int):
        if self.pages_read + pages > self.page_count:
            self.pages_read = self.page_count
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, nut this book has only {self.page_count} pages."
                # self.pages_read = self.page_count
            )
        self.pages_read += pages
        print(f"You have now read  {self.pages_read} out of {self.page_count}.")

class BookShelf():
    def __init__(self,books: List[Book]):
        self.books = books
wiedzmin = Book("Wiedzmin", 350)


# wiedzmin.read(158)
# wiedzmin.read(158)
# wiedzmin.read(158)

try:
    wiedzmin.read(158)
    wiedzmin.read(158)
    wiedzmin.read(158)
except TooManyPagesReadError as e:
    print(e)

print(wiedzmin)