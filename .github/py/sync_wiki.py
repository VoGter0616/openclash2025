import os
import re
import subprocess
import sys

README_PATH = "README.md"
WIKI_DIR = "wiki_repo"

# 1. 定义需要替换进各个标记块的新文本内容（按需修改或从外部文件读取）
OPENCLASH_CONTENT = """这里填入你需要写入 OpenClash 的 Markdown 内容"""
SHADOWROCKET_CONTENT = """这里填入你需要写入 Shadowrocket 的 Markdown 内容"""
SURGE_CONTENT = """这里填入你需要写入 Surge 的 Markdown 内容"""

def run_cmd(cmd, cwd=None):
    res = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"命令执行失败: {cmd}\n错误信息: {res.stderr}")
        sys.exit(1)
    return res.stdout

def replace_between_tags(content, start_tag, end_tag, new_text):
    """
    精准替换 start_tag 与 end_tag 之间的文本内容
    """
    pattern = rf"({re.escape(start_tag)})(.*?)({re.escape(end_tag)})"
    replacement = rf"\1\n{new_text}\n\3"
    
    if not re.search(pattern, content, flags=re.DOTALL):
        print(f"提示: 未在文本中查找到标记 {start_tag} ... {end_tag}")
        return content
        
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def main():
    if not os.path.exists(README_PATH):
        print(f"错误: 找不到 {README_PATH} 文件！")
        return

    # 读取原始 README.md 内容
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # 2. 依次仅替换三大标记块内部的内容
    readme_content = replace_between_tags(
        readme_content, 
        "<!-- OPENCLASH_START -->", 
        "<!-- OPENCLASH_END -->", 
        OPENCLASH_CONTENT.strip()
    )

    readme_content = replace_between_tags(
        readme_content, 
        "<!-- SHADOWROCKET_START -->", 
        "<!-- SHADOWROCKET_END -->", 
        SHADOWROCKET_CONTENT.strip()
    )

    readme_content = replace_between_tags(
        readme_content, 
        "<!-- SURGE_START -->", 
        "<!-- SURGE_END -->", 
        SURGE_CONTENT.strip()
    )

    # 从 GitHub Actions 环境变量获取 token 和仓库名
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")

    if not token or not repo:
        print("错误: 缺少 GH_TOKEN 或 GITHUB_REPOSITORY 环境变量！")
        return

    wiki_url = f"https://x-access-token:{token}@github.com/{repo}.wiki.git"

    print("正在克隆 Wiki 仓库...")
    run_cmd(f"git clone {wiki_url} {WIKI_DIR}")

    # 3. 将更新特定区域后的 README 内容写入 Wiki 首页 Home.md
    home_md_path = os.path.join(WIKI_DIR, "Home.md")
    with open(home_md_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 4. 检查 Wiki 仓库状态并提交
    status = run_cmd("git status --porcelain", cwd=WIKI_DIR)
    if status.strip():
        print("检测到内容变化，准备提交并推送至 Wiki...")
        run_cmd('git config user.name "github-actions[bot]"', cwd=WIKI_DIR)
        run_cmd('git config user.email "github-actions[bot]@users.noreply.github.com"', cwd=WIKI_DIR)
        run_cmd("git add Home.md", cwd=WIKI_DIR)
        run_cmd('git commit -m "chore: auto sync section content to Wiki Home"', cwd=WIKI_DIR)
        run_cmd("git push origin HEAD", cwd=WIKI_DIR)
        print("🎉 Wiki 首页指定段落更新成功！")
    else:
        print("Wiki 内容无变化，无需更新。")

if __name__ == "__main__":
    main()
