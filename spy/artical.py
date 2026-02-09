import requests
from bs4 import BeautifulSoup
import os


def download_dan_koe_article(url):
    # 模拟浏览器请求头，避免被拦截
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    try:
        print(f"🚀 正在尝试访问: {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功

        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. 获取标题
        title = soup.find('h1', class_='post-title').get_text(strip=True)
        print(f"📖 找到文章: {title}")

        # 2. 获取正文内容
        # Substack 的文章内容通常在 class 为 'available-content' 或 'body' 的 div 中
        content_div = soup.find('div', class_='available-content')

        if not content_div:
            # 备选方案：尝试寻找主文章体
            content_div = soup.select_one('.body.markup')

        if content_div:
            # 提取所有段落
            paragraphs = content_div.find_all(['p', 'h2', 'h3', 'ul', 'ol'])
            article_text = f"# {title}\n\n"

            for tag in paragraphs:
                if tag.name.startswith('h'):
                    article_text += f"\n## {tag.get_text(strip=True)}\n\n"
                elif tag.name == 'p':
                    article_text += f"{tag.get_text(strip=True)}\n\n"
                elif tag.name in ['ul', 'ol']:
                    article_text += f"{tag.get_text()}\n\n"

            # 3. 保存到本地文件
            filename = f"{title.replace(' ', '_').lower()}.md"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(article_text)

            print(f"✅ 下载成功！文件保存为: {os.path.abspath(filename)}")
        else:
            print("❌ 未能找到正文内容，可能是页面结构发生了变化或文章受限。")

    except Exception as e:
        print(f"⚠️ 发生错误: {e}")


if __name__ == "__main__":
    target_url = "https://letters.thedankoe.com/p/how-to-fix-your-entire-life-in-1"
    download_dan_koe_article(target_url)