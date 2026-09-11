import os
import re

SRC_PATH = "OpenClash设置.md"
README_PATH = "README.md"

def main():
    if not os.path.exists(SRC_PATH) or not os.path.exists(README_PATH):
        print("错误: 找不到源文件或 README.md")
        return

    # 读取本地 OpenClash设置.md
    with open(SRC_PATH, 'r', encoding='utf-8') as f:
        src_content = f.read().strip()

    with open(README_PATH, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    start_tag = "<!-- OPENCLASH_START -->"
    end_tag = "<!-- OPENCLASH_END -->"

    # 优先匹配 HTML 注释标记区域
    if start_tag in readme_content and end_tag in readme_content:
        pattern = re.compile(f"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
        new_readme = pattern.sub(f"{start_tag}\n\n{src_content}\n\n{end_tag}", readme_content)
    else:
        # 无标记时，从 <p align="center">VoGter的自用模板库</p> 开始替换到文本末尾
        target_head = '<p align="center">VoGter的自用模板库</p>'
        if target_head in readme_content:
            head_idx = readme_content.find(target_head)
            new_readme = readme_content[:head_idx] + src_content + "\n"
        else:
            print("警告: 未在 README.md 中找到替换标记或定位文本，跳过更新。")
            return

    if new_readme != readme_content:
        with open(README_PATH, 'w', encoding='utf-8') as f:
            f.write(new_readme)
        print("README.md 更新完成！")
    else:
        print("内容一致，无需更新。")

if __name__ == "__main__":
    main()
