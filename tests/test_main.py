# Library Checkout System (OOP + Dictionaries + Modular Design)

# Concepts Used:
# - Classes & objects
# - Dictionaries & lists
# - Loops
# - Conditionals
# - Methods with returns
# - Modules



# Project Description
# Simulate a simple library where users can borrow and return books.

# Requirements
# Your final program must:
# ✓ Include a Book class
# - Title, author, available (boolean)
# ✓ Include a Library class
# - Stores books in a dictionary: {book_id: Book_object}
# - Methods: show_books(), borrow_book(), return_book()
# ✓ Include a User class
# - Tracks borrowed books
# - Method: borrow(), return_book()
# ✓ Use user input for:
# - Selecting books
# - Borrowing
# - Returning
# ✓ Use modules
# - models.py — classes
# - library_data.py — starting book list
# - main.py — main loop


from test_models import Library

import sys
import os

# ⬇️Add project root to Python path
PRJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PRJECT_ROOT)

import json
from test_utils import get_data_file

def test_load_books():
    json_file_path = get_data_file("library_books.json")

    with open(json_file_path, "r") as file:
        books = json.load(file)

    assert len(books) > 0
    return books


def update_book_availability(book_id, new_status):
    json_file_path = get_data_file("library_books.json")

    with open(json_file_path, "r") as file:
        books = json.load(file)

    for book in books:
        if book["book_id"] == book_id:
            book["available"] = new_status

    with open("data/library_books.json", "w") as file:
        json.dump(books, file, indent=2)


library = Library(None, None, test_load_books())

while True:
    user_option_choice = input("\nChoose an option: 'b' for borrow, 'r' for return, 'v' for viewing titles, or 'e' for exit:\n").lower()

    if user_option_choice == 'b':

        title = input("\nBook title:\n").title()
        author = input("\nAuthors name:\n").title()

        library = Library(title, author, test_load_books())
        book_id, new_status = library.borrow_book()
    elif user_option_choice == 'r':
        pass
    elif user_option_choice == 'v':
        library.show_books()
    else:
        break

    keep_going = input("\nPress 'e' to exit. Press any other key to return to the main menu:\n").lower()

    if keep_going == 'e':
        break


