import requests
import os

# 社交规则源列表
social_urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Facebook/Facebook.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Instagram/Instagram.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitter/Twitter.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Discord/Discord.list",
    "https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/rule/Clash/Telegram.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Whatsapp/Whatsapp.list"
]

def merge_social_rules():
    social_rules = set()
    for url in social_urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(('#', ';')):
                        social_rules.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    output_dir = "rule/Clash"
    output_path = os.path.join(output_dir, "Social_Merged.list")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Social_Merged_List\n")
        f.write("\n".join(sorted(social_rules)))
    print(f"社交规则合并完成，共 {len(social_rules)} 条，已保存至: {output_path}")

if __name__ == "__main__":
    merge_social_rules()
