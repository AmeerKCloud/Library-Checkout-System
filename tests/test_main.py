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
    
    print("\nLoaded books data:")
    print(books)

    assert len(books) > 0
    

test_load_books()                       #⬅️ Remember to call a function to make use of it.

while True:
    borrow_or_return = input("\nChoose an option: 'b' for borrow, 'r' for return, or 'e' for exit:\n").lower()

    if borrow_or_return == 'b':
        title = input("Book title:\n").title()
        author = input("Authors name:\n").title()
    elif borrow_or_return == 'r':
        pass
    else:
        break

    keep_going = input("Press 'e' to exit. Press any other key to return to the main menu:\n").lower()

    if keep_going == 'e':
        break


