import json

def get_credentials():
    username = input("Username: ")
    password = input("Password: ")
    return username, password


def write_pwdb(username, password):
    pwdb = {username: password}
    path = "./pwdb.json"
    with open(path, "w") as f:
        json.dump(pwdb, f)


username, password = get_credentials()
write_pwdb(username, password)

