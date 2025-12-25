# Here go all of the prototype classes in their testing phase
# before i post them in the final 'models.py' file.


class Library:
    """This class stores books in either a dict. or a list."""
    def __init__(self, json_books_data):
        self.json_books_data = json_books_data
        # self.library = []

    def show_books(self):
        print("\n-----------------------All of our titles:----------------------------:")
        for item in self.json_books_data:
            print("__________________________________________________")
            for key, value in item.items():
                print(f"{key}: {value}")

class Book:
    """Title, author, available (boolean)"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def is_available(self):
        pass


class User:
    """Tracks borrowed books"""
    def __init__(self, user_name):
        self.user_name = user_name
        self.borrowed_books = {}

    def borrow(self):
        pass

    def return_book(self):
        pass