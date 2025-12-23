import os

def get_project_root():
    #
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def get_data_file():
    return os.path.join(get_project_root(), "data", "library_books.json")

print(get_data_file())


