# Utility helper functions shared across the project.
# Includes reusable input validation, formatting, and helper logic.

# NOTE: See breakdown + explanation of below code at the end of this file.

import os

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

#⬇️ This function gets imported & invoked in the other files, with name of intended file in place of paremeter 'filename'
def get_data_file(filename):
    return os.path.join(get_project_root(), "data", filename)




# ______ IMPORTANT: Explanation + Breakdown ______:

# What is the intent behind this code in light of this project?
# - The intent is to retrieve the library books data from the 'library_books.json' file & 
# make it useable within the other files where necessarry, namely 'test_main.py' & 'main.py'

# When using this code within other files, one must import it 1st
