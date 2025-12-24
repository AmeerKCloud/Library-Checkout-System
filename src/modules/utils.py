# Utility helper functions shared across the project.
# Includes reusable input validation, formatting, and helper logic.



import os

def get_project_root():
    #
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def get_data_file(filename):
    return os.path.join(get_project_root(), "data", filename)




