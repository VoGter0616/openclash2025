<p align="center">VoGter自用YAML模板</p>

---

可以参照通用模板进行创建.yml文件

```yaml
name: Update 【1. 规则名称】 Rules          # 【要修改】给工作流起个名字（如：Update Game Rules）
on:
  schedule:
    - cron: '0 4 * * *' # 每天北京时间 12:00 (UTC 4:00) 运行 # 【不用动】定时运行时间
  workflow_dispatch:      # 允许你随时手动点击运行       # 【不用动】手动运行开关

jobs:
  build:
    runs-on: ubuntu-latest                             # # 【不用动】运行环境
    permissions:
      contents: write  # 赋予写入仓库内容的权限         # # 【不用动】写入权限配置
    steps:
      - uses: actions/checkout@v4                      # # 【不用动】拉取仓库代码
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Set up Python                            # # 【不用动】安装 Python 环境
        uses: actions/setup-python@v5
        with:
          python-version: '3.9'
          
      - name: Install dependencies                     # # 【不用动】安装依赖库
        run: |
          python -m pip install --upgrade pip
          pip install requests
          
      - name: Run Merge Script
        run: python .github/py/【2. 你的Python脚本文件名】.py # 【要修改】改成你写好的 Python 脚本文件名（如：merge_game.py）
        
      - name: Commit and Push
        run: |
          git config --global user.name 'github-actions[bot]'               # # 【不用动】
          git config --global user.email 'github-actions[bot]@users.noreply.github.com' # # 【不用动】
          git add rule/Clash/【3. 生成的List文件名】.list  # 【要修改】改成你的 Python 脚本里 output_path 生成的文件名（如：Game_Merged.list）
          git commit -m "Auto update 【4. 提交信息说明】 rules" || exit 0 # 【要修改】改下提交备注（如：Auto update Game rules）
          git push origin main                                              # # 【不用动】
