import urllib.request
import re
import os

URL = "https://raw.githubusercontent.com/VoGter0616/VoGter_Clash/refs/heads/main/OpenClash%E8%AE%BE%E7%BD%AE.md"
README_PATH = "README.md"

def fetch_remote_content():
    """获取远程 URL 的 Markdown 内容"""
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def main():
    if not os.path.exists(README_PATH):
        print(f"错误: 找不到 {README_PATH}")
        return

    print("正在获取远程文件...")
    remote_content = fetch_remote_content().strip()

    with open(README_PATH, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    start_tag = "<!-- OPENCLASH_START -->"
    end_tag = "<!-- OPENCLASH_END -->"

    # 优先匹配 HTML 标记区域
    if start_tag in readme_content and end_tag in readme_content:
        pattern = re.compile(f"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
        new_readme = pattern.sub(f"{start_tag}\n\n{remote_content}\n\n{end_tag}", readme_content)
    else:
        # 如果没有标记，尝试以 <p align="center">VoGter的自用模板库</p> 为起点替换到文件末尾（或替换命中匹配段）
        target_head = '<p align="center">VoGter的自用模板库</p>'
        if target_head in readme_content:
            head_idx = readme_content.find(target_head)
            # 保留目标节点之前的内容，替换后面的内容
            new_readme = readme_content[:head_idx] + remote_content + "\n"
        else:
            print("警告: 未在 README.md 中找到替换标记或目标开头，跳过更新。")
            return

    if new_readme != readme_content:
        with open(README_PATH, 'w', encoding='utf-8') as f:
            f.write(new_readme)
        print("README.md 内容更新成功！")
    else:
        print("内容已是最新，无需更新。")

if __name__ == "__main__":
    main()
