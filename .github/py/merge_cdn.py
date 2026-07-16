import requests
import os

#CDN规则
cdn_urls = [
    "https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/rule/Clash/BitComet_CDN.list",
    "https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/rule/Clash/Steam_CDN.list",
    "https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/rule/Clash/Apple_MS_Direct.list",
    "https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/rule/Clash/Microsoft_CN.list",
    "https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/rule/Clash/Direct.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Nvidia/Nvidia.list"
]

def merge_cdn_rules():
    cdn_rules = set()
    for url in cdn_urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(('#', ';')):
                        cdn_rules.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    output_dir = "rule/Clash"
    output_path = os.path.join(output_dir, "CDN_Merged.list")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# CDN_Merged_List\n")
        f.write("\n".join(sorted(cdn_rules)))
    print(f"CDN规则合并完成，共计 {len(cdn_rules)} 条规则，已保存至: {output_path}")

if __name__ == "__main__":
    merge_cdn_rules()
