from modules.models import Library, Book, User
from modules.utils import UserInputs, get_data_file

import sys
import os

# ⬇️Add project root to Python path
PRJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PRJECT_ROOT)

import json
from modules.utils import get_data_file

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

    print(books)


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
            view_past_transacs = input("Enter 'b' to view all currently borrowed books.\nEnter 'r' to view all returned books:\n").lower()
            
            if view_past_transacs == "b":

                if len(user.user_borrowed_books_data[user_name]) == 0:
                    print("\nThere are currently no borrowed books to show.")
                else:
                    for name, books_list in user.user_borrowed_books_data.items():
                        if name == user_name:
                            print(f"\nAll currently borrowed books history for {name}:")
                            for item in books_list:
                                print("-------------------------------------------------")
                                for key, value in item.items():
                                    print(f"{key}: {value}")


            elif view_past_transacs == "r":

                if len(user.user_returned_books_data[user_name]) == 0:
                    print("\nThere are currently no returned books to show.")
                else:
                    for name, books_list in user.user_returned_books_data.items():
                        if name == user_name:
                            print(f"\nAll returned books history for {name}:")
                            for item in books_list:
                                print("-------------------------------------------------")
                                for key, value in item.items():
                                    print(f"{key}: {value}")

        elif user_option_choice_1 == "e":
            break
