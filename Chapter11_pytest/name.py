from name_function import *

print("press 'Q' to quit")
while True:
    first = input("\nPlease enter your first name: ")
    if first == "Q":
        break
    last = input("Please enter your last name: ")
    if last == "Q":
        break

    formatted_name = get_formatted_name(first, last)
    print(formatted_name)