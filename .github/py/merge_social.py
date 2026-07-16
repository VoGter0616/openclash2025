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
                    # 排除空白行和注释行
                    if line and not line.startswith(('#', ';')):
                        social_rules.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    output_dir = "rule/Clash"
    output_path = os.path.join(output_dir, "Social_Merged.list")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # --- 统计各类规则数量的逻辑 ---
    stats = {
        "DOMAIN": 0,
        "DOMAIN-KEYWORD": 0,
        "DOMAIN-SUFFIX": 0,
        "IP-CIDR": 0,
        "IP-CIDR6": 0,
        "OTHER": 0  # 容错：防止存在其他未知类型
    }

    for rule in social_rules:
        # 按照逗号分割，取第一个元素作为规则类型
        parts = rule.split(',')
        if parts:
            rule_type = parts[0].strip().upper()
            if rule_type in stats:
                stats[rule_type] += 1
            else:
                stats["OTHER"] += 1

    total_count = len(social_rules)

    # 写入文件
    with open(output_path, "w", encoding="utf-8") as f:
        # 写入统计报表头部
        f.write("# Social_Merged_List\n")
        f.write(f"# DOMAIN: {stats['DOMAIN']}\n")
        f.write(f"# DOMAIN-KEYWORD: {stats['DOMAIN-KEYWORD']}\n")
        f.write(f"# DOMAIN-SUFFIX: {stats['DOMAIN-SUFFIX']}\n")
        f.write(f"# IP-CIDR: {stats['IP-CIDR']}\n")
        f.write(f"# IP-CIDR6: {stats['IP-CIDR6']}\n")
        if stats['OTHER'] > 0:
            f.write(f"# OTHER: {stats['OTHER']}\n")
        f.write(f"# TOTAL: {total_count}\n\n")
        
        # 写入排序后的具体规则列表
        f.write("\n".join(sorted(social_rules)))
        
    print(f"社交规则合并完成，共计 {total_count} 条规则，已保存至: {output_path}")

if __name__ == "__main__":
    merge_social_rules()
