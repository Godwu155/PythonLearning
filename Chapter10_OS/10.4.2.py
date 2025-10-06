from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
nuum = json.loads(contents)

print(nuum)