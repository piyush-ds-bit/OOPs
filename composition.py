# Composition means a class is made up of other classes. It’s a "has-a" relationship.
# Encourages code reuse and flexibility — classes are built by combining simpler parts.

class Library:
    def __init__(self):
        self.books = []  # Composition: Library "has-a" list of Book objects

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.get_title())
