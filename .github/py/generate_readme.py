import os

def generate_readme():
    # 1. 定义你的规则目录
    rule_dir = "rule"
    # 将 README.md 的生成路径设定在 rule 文件夹下面
    readme_path = os.path.join(rule_dir, "README.md")
    
    # 2. 完美的居中标题与全新的表格表头
    markdown_content = """<p align="center">VoGter的自用规则库</p>

---

## 📜 Clash规则列表

| 规则文件 | 类型 | 功能说明 |是否需要代理|
| :--- | :---: | :--- |:--- |
"""

    # 3. 自动扫描 rule 目录下的所有 .list 文件
    if os.path.exists(rule_dir):
        files = sorted(os.listdir(rule_dir))
        for file in files:
            if file.endswith('.list'):
                
                # --- 根据你的要求智能定制每一列的内容 ---
                if "ai" in file.lower():
                    note = "自动抓取ai相关域名。"
                    proxy_status = "建议优先使用美国节点，其次使用新加坡，最好不要用香港"
                elif "game" in file.lower():
                    note = "精确匹配游戏服务器，确保联机稳定。"
                    proxy_status = "PROXY"
                elif "social" in file.lower():
                    note = "自动抓取常用社交与短视频媒体域名。"
                    proxy_status = "PROXY"
                else:
                    # 默认其他文件的说明与直连状态
                    note = f"自动抓取 {file.split('.')[0]} 相关域名。"
                    proxy_status = "DIRECT"

                # 拼接超链接（README在rule目录下，使用 ./ 即可）
                file_url = f"./{file}"
                
                # 拼接成完整的表格行（类型固定为 .list）
                markdown_content += f"| [{file}]({file_url}) | .list | {note} | {proxy_status} |\n"
    else:
        markdown_content += "| 暂无文件 | - | 规则目录不存在 | - |\n"

    # 4. 替换为标准的 GitHub 警告框语法
    markdown_content += """
> [!WARNING]
> 
> 仅根据自己使用情况进行更新
> 
> 所有内容均由VoGter收集于互联网，如有侵权告知删。
"""

    # 5. 强行写入 rule/README.md
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(markdown_content.strip() + "\n")
        
    print("/rule/README.md 精美版生成成功！")

if __name__ == "__main__":
    generate_readme()
