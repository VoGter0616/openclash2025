import requests
import os

# 直连规则源列表
direct_urls = [
    "https://raw.githubusercontent.com/VoGter0616/openclash2025/main/rule/Clash/Bank_CN.list",
    "https://raw.githubusercontent.com/VoGter0616/openclash2025/main/rule/Clash/Xiaomi_IoT.list"
]

def merge_direct_rules():
    direct_rules = set()
    for url in direct_urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    line = line.strip()
                    # 仅保留规则行，跳过注释和空行
                    if line and not line.startswith(('#', ';')):
                        direct_rules.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    output_dir = "rule/Clash"
    output_path = os.path.join(output_dir, "Direct_Merged.list")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Direct_Merged_List\n")
        f.write("\n".join(sorted(direct_rules)))
    print(f"直连规则合并完成，共 {len(direct_rules)} 条，已保存至: {output_path}")

if __name__ == "__main__":
    merge_direct_rules()
