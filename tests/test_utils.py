# Utility helper functions shared across the project.
# Includes reusable input validation, formatting, and helper logic.

# NOTE: See breakdown + explanation of below code for importing JSON file data at the end of this file.

from datetime import datetime
import os

def get_project_root():
    return os.path.dirname(os.path.dirname(__file__))

#⬇️ This function gets imported & invoked in other files, with name of intended file in place of paremeter 'filename'
def get_data_file(filename):
    return os.path.join(get_project_root(), "data", filename)



class UserInputs:
    def __init__(self):
        self.title = None
        self.author = None
        self.u_name = None

    def book_title(self):
        while True:
            self.title = input("\nBook title:\n").upper()
            if self.title != "":
                return self.title
            else:
                print("❌ Field cannot be blank.")

    def book_author(self):
        while True:
            self.author = input("\nAuthors name:\n").upper()
            if self.author != "":
                return self.author
            else:
                print("❌ Field cannot be blank.")

    def user_name(self):
        while True:
            self.u_name = input("\nPlease enter your name:\n").title()
            if self.u_name != "":
                return self.u_name
            else:
                print("❌ Field cannot be blank.")

    def date(self):
        while True:
            self.transac_date = input("\nEnter todays date (MM/DD/YYYY):\n")
            if self.transac_date != "":
                return self.transac_date
            else:
                print("❌ Field cannot be blank.")

    def menu_1(self, u_name):
        while True:
            self.menu_1_options = input(f"\nChoose an option, {u_name}:\n'c' for creating a new transaction \n'v' for viewing all previous transactions \n'e' to exit:\n").lower()
            if self.menu_1_options != "" and self.menu_1_options in ["c", "v", "e"]:
                return self.menu_1_options
            else:
                print("❌ Field cannot be blank OR enter only the letter choices provided ('c', 'v', 'e').")
    
    def menu_2(self, u_name):
        while True:
            self.menu_2_options = input(f"\nChoose a transaction type, {u_name}: \n'a' for availability \n'b' for borrow \n'r' for return \n'v' for viewing titles \n'e' to exit to the main menu:\n").lower()
            if self.menu_2_options != "" and self.menu_2_options in ["a", "b", "r", "v", "e"]:
                return self.menu_2_options
            else:
                print("❌ Field cannot be blank OR enter only the letter choices provided ('a', 'b', 'r', 'v', 'e').")




# ______ IMPORTANT: Explanation + Breakdown of JSON file data importing ______:

# What is the intent behind this code in light of this project?
# - The intent is to retrieve the library books data from the 'library_books.json' file & 
# make it useable within the other files where necessarry, namely 'test_main.py' & later 'main.py'

# When using this code within other files, one must import it 1st
# 


# ===============================================================
# 🧠 WHY THIS CODE WORKS & WHAT IT IS DOING (STEP BY STEP)
# ===============================================================

# import os
#📝 The 'os' module gives Python tools to work with folders and file paths
#📝 in a way that works on Windows, macOS, and Linux.

# ---------------------------------------------------------------
# FUNCTION 1: get_project_root()
# ---------------------------------------------------------------
# def get_project_root():
    #📝 __file__ is a special Python variable.
    #📝 It always contains the FULL path of the current file.
    #
    #📝 Example:
    #📝 __file__ might be:
    #📝   C:\Git\Library-Checkout-System\src\modules\path_utils.py
    #
    #📝 os.path.dirname(path) means:
    #📝   "Go UP one folder from this path"
    #     The more times this is layered, the more folders it will traverse from current path.

    #📝 First dirname:
    #📝 path_utils.py  →  modules
    #
    #📝 Second dirname:
    #📝 modules        →  src
    #
    #📝 Third dirname:
    #📝 src            →  project root (Library-Checkout-System)

    # return os.path.dirname(
    #     os.path.dirname(
    #         os.path.dirname(__file__)
    #     )
    # )

#📝 This function works because:
#📝 - It always starts from the CURRENT file's location
#📝 - It moves upward a fixed number of folders
#📝 - It reliably lands at the project root, no matter where the code is run from

# ---------------------------------------------------------------
# FUNCTION 2: get_data_file(filename)
# ---------------------------------------------------------------
# def get_data_file(filename):
    #📝 'filename' is just the NAME of a file inside the 'data' folder
    #📝 Example values:
    #   "library_books.json"
    #   "users.json"
    #   "transactions.json"

    #📝 os.path.join() safely combines folder names into a full path.
    #📝 This avoids hardcoding paths like:
    #📝   "../data/library_books.json"  ❌ (fragile and unsafe)

    # return os.path.join(
    #     get_project_root(),  #⬅️ The main project folder
    #     "data",              #⬅️ The data sub-folder
    #     filename             #⬅️ The specific file you want, in this case "library_books.json"
    # )

# ---------------------------------------------------------------
# 🧠 WHAT THIS CODE ACHIEVES (BIG PICTURE)
# ---------------------------------------------------------------
# 1. It finds the project root dynamically (no hardcoded paths)
# 2. It builds correct file paths regardless of:
#    - Where the script is run from
#    - Which OS is used
#    - Whether the code runs in tests, IDEs, or CI
# 3. It centralizes file-path logic in ONE place
# 4. It prevents FileNotFoundError caused by fragile relative paths

# ---------------------------------------------------------------
# ✅ WHY THIS IS PROFESSIONAL-GRADE CODE
# ---------------------------------------------------------------
# - Portable (works everywhere)
# - Reusable (any data file can be loaded)
# - Test-safe (works from src/, tests/, or elsewhere)
# - Clean separation of responsibility
#
# This is exactly how real-world Python projects locate shared data files.