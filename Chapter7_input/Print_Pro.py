import string
import time
text = input("Enter a string: ")
temp = ""

for ch in text:
    for i in string.printable:
        if ch == i or i == ch:
            time.sleep(0.02)
            print(temp + i)
            temp += ch
            break

        else:
            time.sleep(0.02)
            print(temp + i)

