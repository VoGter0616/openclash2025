name: Sync Settings to README

on:
  push:
    paths:
      - 'OpenClash设置.md'
      - 'Shadowrocket设置.md'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  sync-readme:
    runs-on: ubuntu-latest

    steps:
      - name: 检出代码库
        uses: actions/checkout@v4

      - name: 配置 Python 环境
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: 执行替换脚本
        run: python .github/py/sync_readme.py

      - name: 提交并推送变更
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: auto sync settings files to README.md"
          branch: ${{ github.ref_name }}
