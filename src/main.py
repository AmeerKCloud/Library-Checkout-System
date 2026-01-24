# The final main program for the library checkout system program.
# - To see the prototype/experimental/test code & all explanatory notes, visit the 'tests' folder

from modules.models import Library, Book, User
from modules.utils import UserInputs, Presentation, get_data_file

import sys
import os

# ⬇️Add project root to Python path
PRJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PRJECT_ROOT)

import json

def test_load_books():
    """All the books from the JSON data file."""
    json_file_path = get_data_file("library_books.json")

    with open(json_file_path, "r") as file:
        books = json.load(file)

    assert len(books) > 0
    return books


def update_book_availability(id_book, update_status):
    """Updates the book availability within the JSON data file."""
    json_file_path = get_data_file("library_books.json")

    with open(json_file_path, "r") as file:                     #⬅️ 'r' stands for 'read'?
        books = json.load(file)

    for book in books:
        if book["book_id"] == id_book:
            book["available"] = update_status

    with open(json_file_path, "w") as file:                     #⬅️ 'w' stands for 'write'?
        json.dump(books, file, indent=2)


#--------------------------------- Main Program Below ------------------------------------

library = Library(None, None, test_load_books())
user_inputs = UserInputs()

while True:
    user_name = user_inputs.user_name()
    if user_name == "E":
        break

    while True:
        user = User(user_name, test_load_books())

        user_option_choice_1 = user_inputs.menu_1(user_name)

        if user_option_choice_1 == "c":

            while True:
                user_option_choice_2 = user_inputs.menu_2(user_name)

                if user_option_choice_2 == "a":
                    book = Book(user_inputs.book_title(), user_inputs.book_author(), test_load_books())
                    book.is_available()

                elif user_option_choice_2 == 'b':

                    title = user_inputs.book_title()
                    author = user_inputs.book_author()
                    date = user_inputs.date()

                    library = Library(title, author, test_load_books())
                    book_id, new_status = library.borrow_book()
                    
                    if book_id == False and new_status == False:
                        break
                    else:
                        user.borrow_books(title, author, date)
                        update_book_availability(book_id, new_status) 

                elif user_option_choice_2 == 'r':

                    title = user_inputs.book_title()
                    author = user_inputs.book_author()
                    date = user_inputs.date()

                    library = Library(title, author, test_load_books())
                    book_id, new_status = library.return_book()
                    update_book_availability(book_id, new_status)
                    user.returned_books(title, author, date)

                elif user_option_choice_2 == 'v':
                    library.show_books()
                else:
                    break

        elif user_option_choice_1 == "v":
            presentation = Presentation()

            while True:
                user_option_choice_3 = user_inputs.menu_3(user_name)
                
                if user_option_choice_3 == "b":
                    transac_type = "borrowed"
                    presentation.print_transac_history(user_name, transac_type, user.user_borrowed_books_data)

                elif user_option_choice_3 == "r":
                    transac_type = "returned"
                    presentation.print_transac_history(user_name, transac_type, user.user_returned_books_data)

                elif user_option_choice_3 == "e":
                    break

        elif user_option_choice_1 == "e":
            break


# IMPORTANT: Program still has some issues & bugs:
# - Issue: When you enter a non-existent book/author combo, it takes u back 2 main menu (✅Resolved)
# - - It should infact only take you back to the secondary menu. (✅Resolved)