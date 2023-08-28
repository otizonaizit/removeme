import getpass

def get_credentials():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username, password

get_credentials()
