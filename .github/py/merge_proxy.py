import requests
import os

# Proxy规则
ai_urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Proxy/Proxy.list",
    "https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/rule/Clash/Proxy.list"
]

def merge_proxy_rules():
    ai_rules = set()
    for url in ai_urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(('#', ';')):
                        ai_rules.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    output_dir = "rule/Clash"
    output_path = os.path.join(output_dir, "Custom_Proxy.list")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Proxy_Merged_List\n")
        f.write("\n".join(sorted(ai_rules)))
    print(f"Proxy规则合并完成，共计 {len(ai_rules)} 条规则，已保存至: {output_path}")

if __name__ == "__main__":
    # 🌟 修复：函数名对齐为 merge_proxy_rules()
    merge_proxy_rules()
