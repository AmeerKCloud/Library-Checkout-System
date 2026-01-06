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

    def borrow_book(self):                                                                  #⬅️ Just completed this funct. Appears to be working as intended.
        """"""
        for item in self.json_books_data_list:
            if self.book_title in item.values() and self.book_author in item.values():      #⬅️ '.values()' specifically seeks dict. values only, prone to errors?
                if item["available"] == False:
                    print(f"We're sorry, {self.book_title}, by {self.book_author} is currently unavailable.")
                    return None, None
                else:
                    print(f"\n")
                    for key, value in item.items():
                        print(f"{key}: {value}")

                    print(f"\nYou have now borrowed {self.book_title}, by {self.book_author}")
                    item["available"] = False

                    print("\n")
                    for key, value in item.items():
                        print(f"{key}: {value}")
                    return item["book_id"], item["available"]

    def return_book(self):
        for item in self.json_books_data_list:
            if item["title"] == self.book_title and item["author"] == self.book_author:     #⬅️ This way is better & less prone to errors accordint to ChatGPT.
                # print("Exists")
                if item["available"] == False:
                    item["available"] = True
                    print(f"You have now returned {self.book_title}, by {self.book_author}")
                    return item["book_id"], item["available"]
            else:
                print("NOT exist")

class Book:
    """Title, author, available (boolean)"""
    def __init__(self, title, author, json_books_data_list):
        self.title = title
        self.author = author
        self.json_books_data_list = json_books_data_list

    def is_available(self):
        for item in self.json_books_data_list:
            if item["title"] == self.title and item["author"] == self.author:
                # print("exists")                                                 #⬅️ For testing & validation purposes only.
                if item["available"] == True:
                    print(f"\n{self.title}, by {self.author} is currently available ✅")
                else:
                    print(f"\n{self.title}, by {self.author} is currently NOT available ❌")


class User:                                                             #⬅️ Currently working on this class.
    """Tracks borrowed books"""
    def __init__(self, u_name, json_books_data_list):
        self.u_name = u_name
        self.json_books_data_list = json_books_data_list
        self.user_books_data = {}                                              #⬅️ The main dict., user name as key, list of dict. items as value.

        for key in self.user_books_data:
            if key != self.u_name:                                          #⬅️ If user not already in dict. data, then create username key & assign list as value
                print(f"\n{self.u_name} just added.")
                self.user_books_data[self.u_name] = []                                 #⬅️ Create the user's list ONCE.

    def borrow_books(self, title, author):
        for item in self.json_books_data_list:
            if item["title"] == title and item["author"] == author:
                # Create a NEW book dict each time
                book = {
                    "book_id": item["book_id"],
                    "title": item["title"],
                    "author": item["author"],
                    "genre": item["genre"]
                }

                self.user_books_data[self.u_name].append(book)
                print(f"Borrowed: {title} by {author}")
                break
        print(self.user_books_data)


    def returned_books(self):
        pass


    # TODO:
    # Currently trying to build logic in 'borrow_books()' funct
    # - Logic must create a dict with user name as key and all the books theyve borrowed as dict-list-items inside a list-value
    # - - Find out if nested dict or list with dicts as list-items is the better solution (which is what is currently happening)
    # - - Find out how to retrieve book info and create a dict to add to the 'borrowed_books' empty dict (or list)

    # IMPORTANT: Progress report:
    # - Currently, list appends new dict with most recent borrowed book info, but loses previous one.



    # _________ Reserve code:__________:

    # class User:                                                             #⬅️ Currently working on this class.
    #     """Tracks borrowed books"""
    # def __init__(self, u_name, json_books_data_list):
    #     self.u_name = u_name
    #     self.json_books_data_list = json_books_data_list
    #     self.user_books_data = {}                                              #⬅️ The main dict., user name as key, list of dict. items as value.

    #     self.user_books_data[self.u_name] = []                                 #⬅️ Create the user's list ONCE.

    # def borrow_books(self, title, author):
    #     for item in self.json_books_data_list:
    #         if item["title"] == title and item["author"] == author:
    #             # Create a NEW book dict each time
    #             book = {
    #                 "book_id": item["book_id"],
    #                 "title": item["title"],
    #                 "author": item["author"],
    #                 "genre": item["genre"]
    #             }

    #             self.user_books_data[self.u_name].append(book)
    #             print(f"Borrowed: {title} by {author}")
    #             break
    #     print(self.user_books_data)


    # def returned_books(self):
    #     pass