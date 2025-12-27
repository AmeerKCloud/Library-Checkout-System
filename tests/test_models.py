# Here go all of the prototype classes in their testing phase
# before i post them in the final 'models.py' file.


class Library:
    """This class stores books in either a dict. or a list."""
    def __init__(self, book_title, book_author, json_books_data_list):
        self.book_title = book_title
        self.book_author = book_author
        self.json_books_data_list = json_books_data_list
        # self.library = []

    def show_books(self):
        print("\n-----------------------All of our titles:----------------------------:")
        for item in self.json_books_data_list:
            print("__________________________________________________")
            for key, value in item.items():
                print(f"{key}: {value}")

    def borrow_book(self):
        for item in self.json_books_data_list:
            for key, in item:
                if item[key] == self.book_title:
                    pass                     #⬅️ Currently here. Trying 2 validate users choice in book & author.
        pass

    def return_book(self):
        pass

class Book:
    """Title, author, available (boolean)"""
    def __init__(self, title, author, json_books_data_list):
        self.title = title
        self.author = author
        self.json_books_data_list = json_books_data_list

    def is_available(self):
        pass


class User:
    """Tracks borrowed books"""
    def __init__(self, user_name, json_books_data_list):
        self.user_name = user_name
        self.json_books_data_list = json_books_data_list
        self.borrowed_books = {}

    def borrow(self):
        pass

    def return_book(self):
        pass