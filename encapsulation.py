# Encapsulation means hiding internal details and only exposing what’s necessary.
# In Python, this is done using classes and access modifiers (like _ or __).


class Book:
    def __init__(self, title, author, copies):
        self.__title = title
        self.__author = author
        self.__copies = copies  # private

    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__copies > 0

    def borrow(self):
        if self.__copies > 0:
            self.__copies -= 1
            return True
        return False
