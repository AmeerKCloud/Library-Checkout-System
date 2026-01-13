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


from test_models import Library, Book, User
from test_utils import UserInputs

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


def update_book_availability(id_book, update_status):
    json_file_path = get_data_file("library_books.json")

    with open(json_file_path, "r") as file:                     #⬅️ 'r' stands for 'read'?
        books = json.load(file)

    for book in books:
        if book["book_id"] == id_book:
            book["available"] = update_status

    with open(json_file_path, "w") as file:                     #⬅️ 'w' stands for 'write'?
        json.dump(books, file, indent=2)

    print(books)


#--------------------------------- Main Program Below ------------------------------------

library = Library(None, None, test_load_books())
user_inputs = UserInputs()

while True:
    user_name = user_inputs.user_name()
    if user_name == "e":
        break

    while True:
        user = User(user_name, test_load_books())

        user_option_choice_1 = input(f"\nChoose an option, {user_name}:\n'c' for creating a new transaction \n'v' for viewing all previous transactions \n'e' to exit:\n").lower()

        if user_option_choice_1 == "c":

            while True:
                user_option_choice_2 = input(f"\nChoose a transaction type, {user_name}: \n'a' for availability \n'b' for borrow \n'r' for return \n'v' for viewing titles \n'e' to return to the main menu:\n").lower()

                if user_option_choice_2 == "a":
                    book = Book(user_inputs.book_title(), user_inputs.book_author(), test_load_books())
                    book.is_available()

                elif user_option_choice_2 == 'b':

                    title = user_inputs.book_title()
                    author = user_inputs.book_author()

                    library = Library(title, author, test_load_books())
                    book_id, new_status = library.borrow_book()
                    
                    if book_id == False and new_status == False:
                        break
                    else:
                        user.borrow_books(title, author)
                        update_book_availability(book_id, new_status) 

                elif user_option_choice_2 == 'r':

                    title = user_inputs.book_title()
                    author = user_inputs.book_author()

                    library = Library(title, author, test_load_books())
                    book_id, new_status = library.return_book()
                    update_book_availability(book_id, new_status)
                    user.returned_books(title, author)

                elif user_option_choice_2 == 'v':
                    library.show_books()
                else:
                    break

        elif user_option_choice_1 == "v":                       #⬅️ Currntly here. Wrkng out how 2 view previously borrowed / returned books
            view_past_transacs = input("Enter 'b' to view all currently borrowed books.\nEnter 'r' to view all returned books:\n").lower()
            
            if view_past_transacs == "b":

                if len(user.user_borrowed_books_data[user_name]) == 0:
                    print("\nThere are currently no borrowed books to show.")
                else:
                    for name, books_list in user.user_borrowed_books_data.items():
                        if name == user_name:
                            print(f"\nAll currently borrowed books history for {name}:")
                            for item in books_list:
                                print("-------------------------------------------")
                                for key, value in item.items():
                                    print(f"{key}: {value}")


            elif view_past_transacs == "r":

                if len(user.user_returned_books_data[user_name]) == 0:
                    print("\nThere are currently no returned books to show.")
                else:
                    for name, books_list in user.user_returned_books_data.items():
                        if name == user_name:
                            print(f"\nAll returned books history for {name}:")
                            print(books_list)

        elif user_option_choice_1 == "e":
            break




#--------------------------------- End of Main Program ------------------------------------

# TODO:
# - Refactor code to improve modularity and separation of concerns
# - Add error handling for file operations and user inputs

# Currently program does not catch irrelevant user inputs, like random gibberish
# - Create functionality that checks for this in the 'test_utils.py' file

# Currently user is unable to view their borrowed or returned books history
# - Give the 'test_menu.py' program functionality that allows this
# - Perhaps an if/else statement that lets the user choose from two options:
# - - Option 'a' lets him create a new transaction (the already existed menu)
# - - Option 'b' lets him check all previous transactions (borrowed/returned books)
# - - - Book(s) borrowed, date they were borrowed. Book(s) returned, date they were returned.

# Also:
# - When a user returns a book, it must be removed from the currently borrowed books history
# - When a user borrows a previously returned book & then returns it again, the previous log is kept, 
# new log with new date is added.