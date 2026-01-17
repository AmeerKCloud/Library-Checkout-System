# Here go all of the classes for the 'main.py' library main program.


class Library:
    """This class stores books in either a dict. or a list."""
    def __init__(self, book_title, book_author, json_books_data_list):
        self.book_title = book_title
        self.book_author = book_author
        self.json_books_data_list = json_books_data_list

    def show_books(self):
        print("\n-----------------------All of our titles:----------------------------:")
        for item in self.json_books_data_list:
            print("__________________________________________________")
            for key, value in item.items():
                print(f"{key}: {value}")

    def borrow_book(self):
        """Borrow books."""
        len_book_list = len(self.json_books_data_list)

        while len_book_list > 0:
            print(f"\nSearching for {self.book_title.title()}, by {self.book_author.title()}...")
            for item in self.json_books_data_list:
                len_book_list -= 1
                print(f"Books left to check: {len_book_list}")
                if self.book_title in item.values() and self.book_author in item.values():
                    if item["available"] == False:
                        print(f"We're sorry, {self.book_title}, by {self.book_author} is currently unavailable.")
                        return False, False
                    else:
                        print(f"\n")
                        for key, value in item.items():
                            print(f"{key}: {value}")

                        item["available"] = False

                        print("\n")
                        for key, value in item.items():
                            print(f"{key}: {value}")
                        return item["book_id"], item["available"]
            if len_book_list == 0:
                print(f"\nSorry, we were unable to find {self.book_title.title()}, by {self.book_author.title()}.")
                print("Perhaps check your spelling or review our available list?")
                return False, False

    def return_book(self):
        for item in self.json_books_data_list:
            if item["title"] == self.book_title and item["author"] == self.book_author:
                if item["available"] == False:
                    item["available"] = True
                    print(f"You have now returned {self.book_title.title()}, by {self.book_author.title()}")
                    return item["book_id"], item["available"]

class Book:
    """Title, author, available (boolean)"""
    def __init__(self, title, author, json_books_data_list):
        self.title = title
        self.author = author
        self.json_books_data_list = json_books_data_list

    def is_available(self):
        for item in self.json_books_data_list:
            if item["title"] == self.title and item["author"] == self.author:
                if item["available"] == True:
                    print(f"\n{self.title}, by {self.author} is currently available ✅")
                else:
                    print(f"\n{self.title}, by {self.author} is currently NOT available ❌")


class User:
    """This class contains the functions 
    that track borrowed & returned books"""

    user_borrowed_books_data = {}
    user_returned_books_data = {}

    def __init__(self, u_name, json_books_data_list):

        self.u_name = u_name
        self.json_books_data_list = json_books_data_list

        if not self.u_name in User.user_borrowed_books_data:
            User.user_borrowed_books_data[self.u_name] = []

        if not self.u_name in User.user_returned_books_data:
            User.user_returned_books_data[self.u_name] = []

    def borrow_books(self, title, author, date):
        for item in self.json_books_data_list:
            if item["title"] == title and item["author"] == author:
                book = {
                    "book_id": item["book_id"],
                    "title": item["title"],
                    "author": item["author"],
                    "genre": item["genre"],
                    "borrowed on": date,
                }

                User.user_borrowed_books_data[self.u_name].append(book)
                print(f"\nYou have now borrowed {title}, by {author}")
                break
            
        return User.user_borrowed_books_data


    def returned_books(self, title, author, date):
        """This function tracks returned books"""
        for item in self.json_books_data_list:
            if item["title"] == title and item["author"] == author:
                book = {
                    "book_id": item["book_id"],
                    "title": item["title"],
                    "author": item["author"],
                    "genre": item["genre"],
                    "returned on": date,
                }

                User.user_returned_books_data[self.u_name].append(book)
                print(f"Returned: {title} by {author}, on: {date}")

                if self.u_name in User.user_borrowed_books_data:
                    for item in User.user_borrowed_books_data[self.u_name]: 
                        if item["title"] == title and item["author"] == author:
                            User.user_borrowed_books_data[self.u_name].remove(item)
                break

        return User.user_returned_books_data