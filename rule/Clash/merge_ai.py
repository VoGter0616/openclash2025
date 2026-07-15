import requests

# blackmatrix7 提供的 AI 相关规则链接
ai_urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Gemini/Gemini.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Anthropic/Anthropic.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Mistral/Mistral.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Copilot/Copilot.list"
]

def merge_ai_rules():
    ai_rules = set()
    for url in ai_urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    line = line.strip()
                    # 仅保留规则行，跳过注释和空行
                    if line and not line.startswith(('#', ';')):
                        ai_rules.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    # 保存为统一的 AI.list
    with open("AI_Merged.list", "w", encoding="utf-8") as f:
        f.write("# AI_Merged_List\n")
        f.write("\n".join(sorted(ai_rules)))
    print(f"合并完成，共计 {len(ai_rules)} 条规则。")

if __name__ == "__main__":
    merge_ai_rules()
