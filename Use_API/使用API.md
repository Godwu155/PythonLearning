# 使用API 

2026年2月14日

## 什么是API：

**API**（Application Programming Interface，应用程序编程接口）

API 的核心作用

API 存在的意义在于**简化开发**和**保护隐私**：

- **避免重复造轮子：** 提高效率，直接调用现成的工具去实现预期的功能。
- **安全性：** API已经划定好了访问数据的“深浅”，因此很少出现数据泄密的情况。
- **跨平台连接：** 它可以让手机 App、网页和服务器之间顺畅地传输信息，无论它们使用的是什么编程语言。

## 使用方式

1. 在要获得api的网站官方文档中查找api格式，比如请求头（headers）等。

2. 使用`requests`库请求

   ```python
   import requests
   
   url = "https://api.github.com/search/repositories"
   url += "?q=language:python+sort:stars+stars:>100000"
   
   headers = {"Accept": "application/vnd.github+json"}
   response = requests.get(url, headers=headers)
   ```


------

## 1. Web API 基础概念

**API (Application Programming Interface)** 是程序与程序之间沟通的桥梁。Web API 允许你通过特定的 URL 发送请求，并获取结构化的数据（通常是 JSON 格式）。

- **请求（Request）：** 你的程序向服务器发送一个 URL。
- **响应（Response）：** 服务器返回包含请求信息的文本流。
- **GitHub API：** 本章以 GitHub 为例，调用其搜索接口来获取星标（Star）最多的 Python 项目。

------

## 2. 使用 requests 库

`requests` 是 Python 中最流行、最简单的 HTTP 库，用于发送网络请求。

### 安装

Bash

```bash
pip install requests
```

### 核心操作步骤

1. **导入模块：** `import requests`
2. **存储 URL：** 定义 API 的端点（Endpoint）。
3. **发送请求：** 使用 `requests.get(url)`。
4. **检查状态：** 查看响应对象的 `status_code`（**200** 表示成功）。
5. **处理响应：** 使用 `.json()` 方法将 JSON 格式的响应转换为 Python 字典。



```Python
import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"} # 指定 API 版本
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 将 API 响应转换为字典
response_dict = r.json()
```

------

## 3. 处理响应字典

获取到 `response_dict` 后，需要通过键值对提取有用的信息。

- **`total_count`：** 搜索到的项目总数。
- **`items`：** 一个列表，包含每个仓库的详细信息（每个元素是一个字典）。

### 遍历仓库信息

通常我们需要提取以下字段：

- `name`: 项目名称
- `owner`: 所有者（嵌套字典）
- `stargazers_count`: 星标数
- `html_url`: 项目链接
- `description`: 项目描述

------

## 4. 使用 Plotly 可视化数据

在第 3 版中，作者推荐使用 **Plotly** 来创建交互式图表。

### 准备绘图数据

通过循环从 API 返回的 `items` 中提取数据并存入列表：



```Python
repo_names, stars, labels = [], [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
    # 构建悬停文本：所有者和描述
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)
```

### 创建条形图

使用 `plotly.express` 构建图表：



```Python
import plotly.express as px

# 自定义图表配置
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_names, y=stars, title="Most-Starred Python Projects on GitHub",
             labels=labels, hover_name=labels)

# 优化外观
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()
```

------

## 5. 进阶优化：添加交互连接

为了让图表更有用，可以将条形图的条位设置为可点击的链接，点击后直接跳转到 GitHub 页面。

- **方法：** 在 `repo_names` 列表中存储 HTML 链接格式的字符串，例如：

  `f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>"`

------

## 6. 本章核心知识点总结

| **知识点**        | **描述**                                                     |
| ----------------- | ------------------------------------------------------------ |
| **API 调用限制**  | 大多数 API 都有频率限制（Rate Limit）。GitHub 允许匿名请求，但频率较低。 |
| **JSON 数据结构** | 理解嵌套的字典和列表是处理 API 数据的关键。                  |
| **requests 对象** | `r.status_code` 检查状态，`r.json()` 获取内容。              |
| **Plotly 优势**   | 相比 Matplotlib，Plotly 生成的 HTML 图表支持缩放、悬停查看详情和点击跳转。 |

------

> **避坑指南：**
>
> 如果在调用 API 时遇到 `403` 错误，通常是由于触发了 GitHub 的速率限制。请稍等一分钟再运行，或者在请求头中添加有效的 GitHub Token。

