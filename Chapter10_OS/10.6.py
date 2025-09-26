try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

except ValueError:
    print("Invalid input")

else:
    sum = num1 + num2
    print(f"Sum = {sum}")