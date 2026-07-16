<p align="center">VoGter的规则通用 Python 脚本模板</p>

---

可以参照通用模板进行创建.py脚本

```python
import requests                                                        # # 【不用动】
import os                                                              # # 【不用动】

# 【1. 要修改：在这里放你要合并的规则链接列表】
# 这里的变量名（例如：my_urls）可以自己起，但要跟下面循环里的变量名保持一致
urls_to_merge = [
    "https://example.com/rule1.list",
    "https://example.com/rule2.list"
]

# 【2. 要修改：自定义你的函数名称】（最好英文，拼写无所谓）
def merge_custom_rules():
    # 用于存放去重后规则的集合
    rules_set = set()                                                  # # 【不用动】
    
    # 【3. 要修改：注意这里的循环变量要跟上面 【1】 定义的列表名一致】
    for url in urls_to_merge:
        try:
            response = requests.get(url, timeout=15)                   # # 【不用动】
            if response.status_code == 200:                            # # 【不用动】
                for line in response.text.splitlines():                # # 【不用动】
                    line = line.strip()                                # # 【不用动】
                    # 仅保留规则行，跳过注释和空行
                    if line and not line.startswith(('#', ';')):       # # # 【不用动】
                        rules_set.add(line)                            # # 【不用动】
        except Exception as e:                                         # # 【不用动】
            print(f"Error fetching {url}: {e}")                         # # 【不用动】

    # # 【不用动】统一输出到 rule/Clash 目录下
    output_dir = "rule/Clash"
    
    # 【4. 要修改：这里改成你想要生成的最终文件名】
    output_filename = "My_Custom_Merged.list"
    
    output_path = os.path.join(output_dir, output_filename)            # # 【不用动】

    # 自动创建目录                                                       # # 【不用动】
    if not os.path.exists(output_dir):                                 # # 【不用动】
        os.makedirs(output_dir)                                        # # 【不用动】

    # 🌟 【不用动】全新加入：全自动统计各类规则数量的逻辑
    stats = {
        "DOMAIN": 0,
        "DOMAIN-KEYWORD": 0,
        "DOMAIN-SUFFIX": 0,
        "IP-CIDR": 0,
        "IP-CIDR6": 0,
        "OTHER": 0  # 容错：防止存在其他未知类型
    }

    for rule in rules_set:
        # 按照逗号分割，取第一个元素作为规则类型
        parts = rule.split(',')
        if parts:
            rule_type = parts[0].strip().upper()
            if rule_type in stats:
                stats[rule_type] += 1
            else:
                stats["OTHER"] += 1

    total_count = len(rules_set)

    # 保存文件                                                         # # 【不用动】
    with open(output_path, "w", encoding="utf-8") as f:                # # 【不用动】
        # 🌟 自动生成带格式统计的文件头部
        f.write(f"# {output_filename.split('.')[0]}\n")
        f.write(f"# DOMAIN: {stats['DOMAIN']}\n")
        f.write(f"# DOMAIN-KEYWORD: {stats['DOMAIN-KEYWORD']}\n")
        f.write(f"# DOMAIN-SUFFIX: {stats['DOMAIN-SUFFIX']}\n")
        f.write(f"# IP-CIDR: {stats['IP-CIDR']}\n")
        f.write(f"# IP-CIDR6: {stats['IP-CIDR6']}\n")
        if stats['OTHER'] > 0:
            f.write(f"# OTHER: {stats['OTHER']}\n")
        f.write(f"# TOTAL: {total_count}\n\n")
        
        # 写入排序后的具体规则列表
        f.write("\n".join(sorted(rules_set)))                          # # 【不用动】
        
    # 【5. 要修改：改一下控制台输出的提示文字，方便在 GitHub Actions 日志里查看】
    print(f"合并完成，共计 {total_count} 条规则，已保存至: {output_path}")

if __name__ == "__main__":                                             # # 【不用动】
    # 【6. 要修改：这里的函数名必须和上面 【2】 定义的函数名完全一致】
    merge_custom_rules()
