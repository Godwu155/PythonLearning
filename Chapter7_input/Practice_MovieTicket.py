

prompt = "Please enter your age:"
# message = ""
age = ""

active = True

while age != "quit":
    age = int(input(prompt))
    if age <3:
        print("Your ticket is free!")

    elif age >12:
        print("Your ticket is 15$")

    else:
        print("Your ticket is 10$!")

    break



