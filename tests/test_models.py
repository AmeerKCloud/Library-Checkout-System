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

    #⬇️'user_books_data' initiated as a class variable. A class variable belongs to the class itself, not individual objects, & can be shared by all objects
    user_books_data = {}                                              #⬅️ The main dict., user name as key, list of dict. items as value.

    def __init__(self, u_name, json_books_data_list):

        #⬇️ An instance variable belongs to one specific object created from a class. Each object gets its own copy.
        self.u_name = u_name                                  #⬅️ instance variable
        self.json_books_data_list = json_books_data_list      #⬅️ instance variable

        if not self.u_name in self.user_books_data:
            print(f"\nJust added {self.u_name}")
            User.user_books_data[self.u_name] = []

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

                User.user_books_data[self.u_name].append(book)
                print(f"Borrowed: {title} by {author}")
                break
        print(User.user_books_data)


    def returned_books(self):
        pass


# TODO:
# Currently trying to build logic in 'borrow_books()' funct
# - Logic must create a dict with user name as key and all the books theyve borrowed as dict-list-items inside a value-list
# - - Find out if nested dict or list with dicts as list-items is the better solution (which is what is currently happening)
# - - Find out how to retrieve book info and create a dict to add to the 'borrowed_books' empty dict (or list)

# IMPORTANT: Progress report:
# - Currently, list appends new dict with most recent borrowed book info, but loses previous one.
# - - Trying to resolve this, by checking the main data dict if username already exists as a key
# - - - If it does, then proceed to just append the new book title to the already existing users book-list
# - - - Else, create the new username key and corresponding empty list and append the first book title to the list.
# NOTE: This problem has now been resoled ✅:
# ❌ The issue was that the main data dict. was created as an 'instance variable' using 'self.', ie (self.user_books_data)
# - This means that it is exclusive to only one object at a time when that object is created, & cannot be shared by multiple objects
# - An instance variable belongs to one specific object created from a class. Each object gets its own copy.
# ✅ The solution in this case was to initiate the data dict as a 'class variable' without the 'self.', ie (user_books_data = {})



# _________ Reserve code:__________:

