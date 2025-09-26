while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break
            x = int(x)

            y = input("\nGive me a number: ")
            if y == 'q':
                break
    except ValueError:
        print("Invalid input")
    else:
        sum = x + y
        print("The sum is:", sum)