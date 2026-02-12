import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>100000"

headers = {"Accept": "application/vnd.github+json"}
response = requests.get(url, headers=headers)
print(f"status_code:{response.status_code}")

response_json = response.json()
print(f"total_count:{response_json['total_count']}")
print(f"Complete result:{response_json['incomplete_results']}")

repos_dicts = response_json['items']
print(f"Repositories:{len(repos_dicts)}")

repos_dict = repos_dicts[0]
print(f"\nKeys:{len(repos_dict)}")
for key in sorted(repos_dict.keys()):
    print(key)
