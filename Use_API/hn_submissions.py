from operator import itemgetter
import requests

# 1. 获取所有热门文章 ID
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submissions_ids = r.json()
submissions_dicts = []

# 2. 【关键修改】使用切片 [:30]，只取前 30 个，否则要等好几分钟
for submission_id in submissions_ids[:30]:
    # 创建每个文章的特定 API URL
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)

    # 打印进度，这样你就知道程序没死
    print(f"Loading item {submission_id}... Status: {r.status_code}")

    response_dict = r.json()

    # 3. 【健壮性】使用 .get() 处理可能缺失的键
    # 有些帖子（如 Job）没有 descendants（评论数）字段
    submissions_dict = {
        "title": response_dict.get("title", "No Title"),
        "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get("descendants", 0),  # 如果没有该键，默认为 0
    }

    submissions_dicts.append(submissions_dict)

# 4. 【逻辑修改】按评论数（comments）降序排列
submissions_dicts.sort(key=itemgetter("comments"), reverse=True)

# 5. 打印结果
for submission in submissions_dicts:
    print(f"\nTitle: {submission['title']}")
    print(f"HN Link: {submission['hn_link']}")
    print(f"Comments: {submission['comments']}")