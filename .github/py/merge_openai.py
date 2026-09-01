import os
from datetime import datetime, timezone, timedelta
import requests

# 稳定的远程 OpenAI 规则源地址
ai_urls = [
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/OpenAi.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/OpenAI/OpenAI.list",
]

VALID_PREFIXES = (
    "DOMAIN",
    "DOMAIN-SUFFIX",
    "DOMAIN-KEYWORD",
    "IP-CIDR",
    "IP-CIDR6",
    "PROCESS-NAME",
)

def get_beijing_time():
    """获取当前的北京时间字符串 (UTC+8)"""
    utc_now = datetime.now(timezone.utc)
    beijing_now = utc_now.astimezone(timezone(timedelta(hours=8)))
    return beijing_now.strftime("%Y-%m-%d %H:%M:%S")

def parse_rule_line(line):
    """提取并清洗行字符，自动将 +.domain 转化为 DOMAIN-SUFFIX,domain"""
    line = line.strip()
    if not line or line.startswith(("#", ";", "payload:", "-")):
        return None
    
    if line.startswith("+."):
        domain = line[2:].strip()
        return f"DOMAIN-SUFFIX,{domain}"
    
    if line.startswith(VALID_PREFIXES):
        return line
        
    return None

def merge_openai_rules():
    output_dir = "rule/Merged"
    output_filename = "OpenAI_Merged.list"
    output_path = os.path.join(output_dir, output_filename)

    # 1. 读取旧文件用于增量比对
    old_rules = set()
    if os.path.exists(output_path):
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    rule = parse_rule_line(line)
                    if rule:
                        old_rules.add(rule)
        except Exception as e:
            print(f"读取旧文件失败: {e}")

    # 2. 抓取最新远程规则
    new_rules = set()
    for url in ai_urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    rule = parse_rule_line(line)
                    if rule:
                        new_rules.add(rule)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    # 3. 追加本地 Perplexity 等补丁域名
    for raw_domain in manual_ai_domains:
        rule = parse_rule_line(raw_domain)
        if rule:
            new_rules.add(rule)

    added_count = len(new_rules - old_rules)

    # 4. 统计类型数量
    stats = {
        "DOMAIN": 0,
        "DOMAIN-KEYWORD": 0,
        "DOMAIN-SUFFIX": 0,
        "IP-CIDR": 0,
        "IP-CIDR6": 0,
        "OTHER": 0,
    }

    for rule in new_rules:
        parts = rule.split(",")
        if parts:
            rule_type = parts[0].strip().upper()
            if rule_type in stats:
                stats[rule_type] += 1
            else:
                stats["OTHER"] += 1

    total_count = len(new_rules)
    updated_at = get_beijing_time()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 5. 写入规则列表文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# {output_filename.split('.')[0]}\n")
        f.write(f"# UPDATED: {updated_at} (UTC+8)\n")
        f.write(f"# DOMAIN: {stats['DOMAIN']}\n")
        f.write(f"# DOMAIN-KEYWORD: {stats['DOMAIN-KEYWORD']}\n")
        f.write(f"# DOMAIN-SUFFIX: {stats['DOMAIN-SUFFIX']}\n")
        f.write(f"# IP-CIDR: {stats['IP-CIDR']}\n")
        f.write(f"# IP-CIDR6: {stats['IP-CIDR6']}\n")
        if stats["OTHER"] > 0:
            f.write(f"# OTHER: {stats['OTHER']}\n")
        f.write(f"# NEWLY ADDED: {added_count}\n")
        f.write(f"# TOTAL: {total_count}\n\n")

        for rule in sorted(new_rules):
            f.write(f"{rule}\n")

    print(
        f"OpenAI规则合并完成！\n"
        f"保存位置: {output_path}\n"
        f"更新时间: {updated_at}\n"
        f"当前总计: {total_count} 条 | 相比上次新增: {added_count} 条"
    )

if __name__ == "__main__":
    merge_openai_rules()
