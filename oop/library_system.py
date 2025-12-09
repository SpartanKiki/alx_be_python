# library_system.py

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"


class PrintBook(Book):
    def __init__(self, title, author, pages, cover_type):
        super().__init__(title, author, pages)
        self.cover_type = cover_type

    def __str__(self):
        base = super().__str__()
        return f"{base} (Print: {self.cover_type} cover)"


class EBook(Book):
    def __init__(self, title, author, pages, file_format):
        super().__init__(title, author, pages)
        self.file_format = file_format

    def __str__(self):
        base = super().__str__()
        return f"{base} (EBook: {self.file_format})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            return "Library is empty."

        return "\n".join(str(book) for book in self.books)
