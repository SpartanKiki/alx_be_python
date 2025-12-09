# main.py

from library_system import Book, PrintBook, EBook, Library

def main():
    library = Library()

    # Create book instances
    book1 = Book("Things Fall Apart", "Chinua Achebe", 209)
    book2 = PrintBook("Harry Potter", "J.K. Rowling", 340, "Hard")
    book3 = EBook("Atomic Habits", "James Clear", 250, "PDF")

    # Add them to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Print output
    print(library.list_books())


if __name__ == "__main__":
    main()
