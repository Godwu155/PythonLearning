from pathlib import Path
import json

path = Path("Love.json")
contents = path.read_text()
num = json.loads(contents)

print(num)