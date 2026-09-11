import os
import re

README_FILE = "README.md"

# 配置需要同步的文件及对应的 HTML 标记
SYNC_CONFIGS = [
    {
        "file": "OpenClash设置.md",
        "start_tag": "<!-- OPENCLASH_START -->",
        "end_tag": "<!-- OPENCLASH_END -->",
    },
    {
        "file": "Shadowrocket设置.md",
        "start_tag": "<!-- SHADOWROCKET_START -->",
        "end_tag": "<!-- SHADOWROCKET_END -->",
    },
]

def main():
    if not os.path.exists(README_FILE):
        print("错误: 找不到 README.md，请检查文件位置！")
        return

    with open(README_FILE, "r", encoding="utf-8") as f:
        readme_content = f.read()

    new_readme = readme_content

    for config in SYNC_CONFIGS:
        file_path = config["file"]
        start_tag = config["start_tag"]
        end_tag = config["end_tag"]

        if not os.path.exists(file_path):
            print(f"提示: 未找到文件 {file_path}，跳过该项同步。")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            source_content = f.read().strip()

        if start_tag in new_readme and end_tag in new_readme:
            pattern = re.compile(f"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
            new_readme = pattern.sub(f"{start_tag}\n\n{source_content}\n\n{end_tag}", new_readme)
            print(f"已同步 [{file_path}] -> README.md")
        else:
            print(f"警告: README.md 中未找到标记 {start_tag} ... {end_tag}")

    # 若内容有改变则写回文件
    if new_readme != readme_content:
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("README.md 更新成功！")
    else:
        print("README.md 内容已是最新，无需更新。")

if __name__ == "__main__":
    main()
