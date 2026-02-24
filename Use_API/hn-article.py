import requests
import json
from pathlib import Path

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

path = Path("Use_API/file/save.json")

response_json = r.json()
response_string = json.dumps(response_json, indent=4)
print(response_string)