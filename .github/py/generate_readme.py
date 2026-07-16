import os

def generate_readme():
    # 1. 定义你的仓库根目录和规则目录
    rule_dir = "rule/Clash"
    readme_path = "README.md"
    
    # 2. 准备 Markdown 的头部内容
    markdown_content = """# 📂 VoGter 的自用规则仓库

> 🤖 本 README 文件由 GitHub Actions 自动构建生成，请勿手动修改。

## 📜 规则列表

| 规则文件 | 类型 | 功能说明 |
| :--- | :---: | :--- |
"""

    # 3. 自动扫描 rule/Clash 目录下的所有 .list 文件
    if os.path.exists(rule_dir):
        files = sorted(os.listdir(rule_dir))
        for file in files:
            if file.endswith('.list'):
                # 根据文件名自动判断是 PROXY 还是 DIRECT
                if "direct" in file.lower() or "cdn" in file.lower():
                    badge = "![](https://img.shields.io/badge/Mode-DIRECT-green?style=flat-square)"
                    note = f"🎯 **直连规则**：自动同步的 {file} 直连分流列表。"
                else:
                    badge = "![](https://img.shields.io/badge/Mode-PROXY-blue?style=flat-square)"
                    note = f"🚀 **非直连规则**：自动同步的 {file} 代理分流列表。"
                
                # 特殊文件名定制特殊说明（可根据你的文件名自行修改）
                if "game" in file.lower():
                    note = "🎮 **游戏规则**：精确匹配游戏服务器，确保联机稳定。"
                elif "ai" in file.lower():
                    note = "✨ **AI 规则**：包含 ChatGPT / Claude 等人工智能常用域名。"

                # 拼接成一条表格行
                file_url = f"./{rule_dir}/{file}"
                markdown_content += f"| [{file}]({file_url}) | {badge} | {note} |\n"
    else:
        markdown_content += "| 暂无文件 | - | 规则目录不存在 |\n"

    # 4. 加上你的底部警告或说明
    markdown_content += """
---

### ⚠️ Warning
仅根据自己使用情况进行更新，所有内容均由 VoGter 收集于互联网，如有侵权告知删。
"""

    # 5. 强行写入根目录的大写 README.md
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(markdown_content.strip() + "\n")
        
    print("Base README.md 生成成功！")

if __name__ == "__main__":
    generate_readme()
