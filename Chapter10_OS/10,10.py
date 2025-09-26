from pathlib import Path

word = input("which word do you want to count: ")

txt_path = Path('Book.txt')
contents = txt_path.read_text(encoding='utf-8')

num = contents.lower().count(word)
print(num)