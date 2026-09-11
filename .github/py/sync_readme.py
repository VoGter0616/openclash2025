import os
import re

# 定义需要同步更新的所有 README 文件路径
TARGET_READMES = ["README.md", "cfg/README.md"]

# 配置源文件与其对应的 HTML 标记
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
    {
        "file": "Surge设置.md",
        "start_tag": "<!-- SURGE_START -->",
        "end_tag": "<!-- SURGE_END -->",
    },
]

def update_readme_file(readme_path):
    if not os.path.exists(readme_path):
        print(f"提示: 找不到文件 {readme_path}，跳过同步。")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    new_readme = readme_content

    for config in SYNC_CONFIGS:
        source_file = config["file"]
        start_tag = config["start_tag"]
        end_tag = config["end_tag"]

        if not os.path.exists(source_file):
            print(f"提示: 找不到源文件 {source_file}，跳过。")
            continue

        with open(source_file, "r", encoding="utf-8") as f:
            source_content = f.read().strip()

        if start_tag in new_readme and end_tag in new_readme:
            pattern = re.compile(f"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
            new_readme = pattern.sub(f"{start_tag}\n\n{source_content}\n\n{end_tag}", new_readme)
            print(f"成功处理: [{source_file}] -> [{readme_path}]")
        else:
            print(f"警告: [{readme_path}] 中未找到标记 {start_tag} ... {end_tag}")

    if new_readme != readme_content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_readme)
        print(f"写入成功: [{readme_path}] 已完成更新！\n")
    else:
        print(f"跳过写入: [{readme_path}] 内容已是最新。\n")

def main():
    for readme_path in TARGET_READMES:
        update_readme_file(readme_path)

if __name__ == "__main__":
    main()
