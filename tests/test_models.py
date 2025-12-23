# Here go all of the prototype classes in their testing phase
# before i post them in the final file.

import json
from src.modules.utils import get_data_file

def test_load_books():
    json_file_path = get_data_file("library_books.json")

    with open(json_file_path, "r") as file:
        books = json.load(file)

    assert len(books) > 0



# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def is_available(self):
#         pass


# class User:
#     def __init__(self):
#         self.borrowed_books = {}

#     def borrow(self):
#         pass

#     def return_book(self):
#         pass