from pathlib import Path
import json

numbers = [1,2,3,4,5,6,7,8,9]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)


# path2 = Path('C:/Users\ROG\PycharmProjects\PythonLearnProject\Chapter10_OS/numbers.json')
# cont2 = path2.read_text()
# text = json.load(cont2)
# print(text)

