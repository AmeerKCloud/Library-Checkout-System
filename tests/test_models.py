# Here go all of the prototype classes in their testing phase
# before i post them in the final file.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def is_available(self):
        pass


class User:
    def __init__(self):
        self.borrowed_books = {}