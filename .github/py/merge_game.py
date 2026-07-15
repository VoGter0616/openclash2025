import requests
import os

# 游戏规则源列表
game_urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Steam/Steam.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Epic/Epic.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Nintendo/Nintendo.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/EA/EA.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Sony/Sony.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Blizzard/Blizzard.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Ubisoft/Ubisoft.list"
]

def merge_game_rules():
    game_rules = set()
    for url in game_urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    line = line.strip()
                    # 仅保留规则行
                    if line and not line.startswith(('#', ';')):
                        game_rules.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    output_dir = "rule/Clash"
    output_path = os.path.join(output_dir, "Game_Merged.list")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Game_Merged_List\n")
        f.write("\n".join(sorted(game_rules)))
    print(f"游戏规则合并完成，共 {len(game_rules)} 条，已保存至: {output_path}")

if __name__ == "__main__":
    merge_game_rules()
