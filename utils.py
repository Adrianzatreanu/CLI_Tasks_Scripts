import os

def clear_screen():
    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux (here, os.name is 'posix')
    else:
        os.system('clear')

def check_db_exists(path):
    return os.path.exists(path)
