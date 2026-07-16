import os
import re

def generate_readme():
    scan_dir = "rule/Clash"   # 扫描的目录
    rule_dir = "rule"         # README 所在的目录
    readme_path = os.path.join(rule_dir, "README.md")
    
    # 用来存储已有文件的“功能说明”和“是否需要代理” {文件名: (功能说明, 是否需要代理)}
    existing_data = {}
    
    # 1. 尝试读取现有的 README.md，提取出已经手工改好的数据
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # 🌟 升级正则：将原先写死的 \.list 改为匹配任意后缀（如 .list 或 .yaml）
                match = re.match(r"\|\s*\[([^\]]+)\]\([^)]+\)\s*\|\s*(\.[a-zA-Z0-9]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|", line)
                if match:
                    filename = match.group(1).strip()
                    # group(2) 是文件后缀，这里我们不需要，直接取说明和代理状态
                    note = match.group(3).strip()
                    proxy_status = match.group(4).strip()
                    existing_data[filename] = (note, proxy_status)

    # 2. 严格还原你的 Markdown 表头模板
    markdown_content = """<p align="center">VoGter的自用规则库</p>

---

## 📜 Clash规则列表

| 规则文件 | 类型 | 功能说明 |是否需要代理|
| :--- | :---: | :--- |:--- |
"""

    # 3. 扫描 rule/Clash 文件夹下的所有文件
    if os.path.exists(scan_dir):
        # 🌟 升级扫描：同时抓取 .list 和 .yaml 文件
        files = sorted([f for f in os.listdir(scan_dir) if f.endswith('.list') or f.endswith('.yaml')])
        
        for file in files:
            file_url = f"./Clash/{file}"
            # 动态获取当前文件的真实后缀（例如 .list 或 .yaml）
            _, ext = os.path.splitext(file)
            
            # 判断这个文件是否已经是历史数据
            if file in existing_data:
                # 如果是已有的数据，原封不动继承你之前的修改
                note, proxy_status = existing_data[file]
            else:
                # 如果是最新抓取到的全新文件，功能说明和是否需要代理留空
                note = ""
                proxy_status = ""
            
            # 🌟 拼接成标准的表格行（类型列动态填入真实后缀）
            markdown_content += f"| [{file}]({file_url}) | {ext} | {note} | {proxy_status} |\n"
            
    else:
        markdown_content += "| 暂无文件 | - | 规则目录不存在 | - |\n"

    # 4. 严格还原你的底部警告框模板
    markdown_content += """
> [!WARNING]
> 
> 仅根据自己使用情况进行更新
> 
> 所有内容均由VoGter收集于互联网，如有侵权告知删。
"""

    # 5. 强行写入到 rule/README.md 
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(markdown_content.strip() + "\n")
        
    print(f"增量同步成功！共整理 {len(files)} 个文件。历史修改已保留，新文件已留空。")

if __name__ == "__main__":
    generate_readme()
