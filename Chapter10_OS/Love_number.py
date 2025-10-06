from pathlib import Path
import json

"""
num1 = input("Enter your love number: ")

path = Path("Love.json")
contents = json.dumps(num1)
path.write_text(contents)

"""


def input_num():
    path = Path("Love_number.json")

    num = input("Enter your love number: ")
    contents = json.dumps(num)
    path.write_text(contents)


def out_num(path):
    if path.exists():
        contents = path.read_text()
        num = json.loads(contents)

        return num
    else:

        input_num()
        raise FileNotFoundError


def say_num(num):
    print(f"The love number is: {num}")

# input_num()
while True:



