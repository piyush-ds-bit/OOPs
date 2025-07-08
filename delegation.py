# Delegation means handing over responsibility to another object/class.
# Helps divide responsibilities cleanly between components.

from composition import Library

class LibrarySystem:
    def __init__(self):
        self.library = Library()  # Delegates to Library
        self.users = []

    def register_user(self, user):
        self.users.append(user)

    def borrow_book(self, user, book_title):
        for book in self.library.books:
            if book.get_title() == book_title:
                if book.borrow():
                    print(f"{user.name} borrowed '{book_title}'")
                    return
        print("Book not available")
