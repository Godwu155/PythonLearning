from pathlib import Path
import json



# username = input("What is your name? ")

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        # print(contents)
        username = json.loads(contents)
        return username
    else:
        return None
#
# path.write_text(contents)
#
#
def greet_user():
    path = Path('Usernames.json')
    username = get_stored_username(path)

    if username:
        print(f"Welcome, {username}!")

    else:
        username = input("What is your name? ")
        contents = json.dumps(username.title())
        path.write_text(contents)
        print(f"We will remember you when you come back,{username.title()}")

# greet_user()

greet_user()


