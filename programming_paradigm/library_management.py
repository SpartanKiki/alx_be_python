class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if book is NOT checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        """Find a book by title and check it out if available."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return

    def return_book(self, title):
        """Find a book by title and return it."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Print only books that are available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
