import os

def get_project_root():
    #
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def get_data_file(filename):
    return os.path.join(get_project_root(), "data", filename)

get_data_file("library_books.json")


