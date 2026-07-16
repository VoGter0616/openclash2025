import os

def generate_readme():
    # 🌟 正确的路径配置：
    scan_dir = "rule/Clash"   # 扫描这个目录下的 .list 文件
    rule_dir = "rule"         # README 所在的父目录
    readme_path = os.path.join(rule_dir, "README.md") # 最终写入 rule/README.md
    
    # 严格还原你的 Markdown 表头模板
    markdown_content = """<p align="center">VoGter的自用规则库</p>

---

## 📜 Clash规则列表

| 规则文件 | 类型 | 功能说明 |是否需要代理|
| :--- | :---: | :--- |:--- |
"""

    # 扫描 rule/Clash 文件夹下的所有文件
    if os.path.exists(scan_dir):
        # 过滤出所有以 .list 结尾的文件，并按字母排序
        files = sorted([f for f in os.listdir(scan_dir) if f.endswith('.list')])
        
        for file in files:
            # 🌟 修复超链接：因为 README 在 rule 目录下，而文件在 rule/Clash 目录下，
            # 所以链接必须写成 ./Clash/文件名.list 才能正确跳转
            file_url = f"./Clash/{file}"
            
            # 严格匹配你的具体文件归类逻辑
            if "ai" in file.lower():
                note = "自动抓取ai相关域名。"
                proxy_status = "建议优先使用美国节点，其次使用新加坡，最好不要用香港"
            else:
                note = "自动抓取ai相关域名。"
                proxy_status = "DIRECT"
            
            # 拼接成标准的表格行
            markdown_content += f"| [{file}]({file_url}) | .list | {note} | {proxy_status} |\n"
            
    else:
        markdown_content += "| 暂无文件 | - | 规则目录不存在 | - |\n"

    # 严格还原你的底部警告框模板
    markdown_content += """
> [!WARNING]
> 
> 仅根据自己使用情况进行更新
> 
> 所有内容均由VoGter收集于互联网，如有侵权告知删。
"""

    # 写入到 rule/README.md 
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(markdown_content.strip() + "\n")
        
    print(f"成功！已自动将 {len(files)} 个 .list 文件归类写入 /rule/README.md")

if __name__ == "__main__":
    generate_readme()
