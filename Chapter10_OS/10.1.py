from pathlib import Path
import re

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

contents.rstrip()
# print(contents)

line = contents.splitlines()

# for line in line:
#     print(line+"\n")

pi_string = ''
for line in line:
    pi_string += line.lstrip()
pi_string.replace(' ', '')


# print(f"pi_string: {pi_string[ :52]}")
# print(len(pi_string))

birthday = input('Enter birthday: ')
if birthday in pi_string:
    print('Yes')
else:
    print('No')



